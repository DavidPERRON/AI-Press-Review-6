from ai_press_review.collect import (
    _ai_relevance_score,
    _contains_banned_topic,
    _is_duplicate_of_previous,
    _score_source,
)
from ai_press_review.models import SourceItem
from ai_press_review.settings import ScoringConfig


def _default_scoring() -> ScoringConfig:
    return ScoringConfig(
        min_relevance=3.0,
        min_text_length=180,
        similarity_threshold=0.88,
        banned_terms=["policy", "regulation", "rumor"],
        ai_terms_high=["artificial intelligence", "generative ai", "large language model"],
        ai_terms_mid=["ai", "llm", "agent", "inference", "benchmark"],
        ai_terms_low=["model", "chip", "research"],
        signal_words_strong=["benchmark", "launch", "funding", "deploy", "training"],
        signal_words_medium=["latency", "chip", "model", "agent", "research"],
        domain_authority={"openai.com": 2.0, "arxiv.org": 1.5},
    )


def _make_source(**kwargs) -> SourceItem:
    defaults = {
        "url": "https://example.com/article",
        "title": "AI model achieves new benchmark",
        "domain": "example.com",
        "published_at": "2026-04-12T10:00:00Z",
        "summary": "A new AI model has set records on major benchmarks.",
        "content_text": "Detailed article content about AI advances " * 50,
    }
    defaults.update(kwargs)
    return SourceItem(**defaults)


def test_contains_banned_topic_positive():
    scoring = _default_scoring()
    assert _contains_banned_topic("New AI regulation policy announced", scoring) is True


def test_contains_banned_topic_negative():
    scoring = _default_scoring()
    assert _contains_banned_topic("OpenAI launches new model", scoring) is False


def test_ai_relevance_high():
    scoring = _default_scoring()
    score = _ai_relevance_score(["artificial intelligence breakthrough"], scoring)
    assert score >= 3.0


def test_ai_relevance_none():
    scoring = _default_scoring()
    score = _ai_relevance_score(["cooking recipe for pasta"], scoring)
    assert score == 0.0


def test_score_source_rich_content():
    scoring = _default_scoring()
    item = _make_source(content_text="benchmark launch funding deploy " * 100)
    score = _score_source(item, scoring)
    assert score >= 5.0


def test_score_source_poor_content():
    scoring = _default_scoring()
    item = _make_source(title="random news story", content_text="short", summary="short")
    score = _score_source(item, scoring)
    assert score < 5.0


def test_score_source_domain_authority():
    scoring = _default_scoring()
    item_auth = _make_source(domain="openai.com")
    item_unknown = _make_source(domain="randomsite.xyz")
    assert _score_source(item_auth, scoring) > _score_source(item_unknown, scoring)


def test_is_duplicate_fingerprint():
    item = _make_source()
    from ai_press_review.utils import fingerprint
    fp = fingerprint(item.title, item.url)
    assert _is_duplicate_of_previous(item, {fp}, [], [], 0.88) is True


def test_is_duplicate_similar_title():
    item = _make_source(title="OpenAI launches GPT-5 model")
    assert _is_duplicate_of_previous(item, set(), ["OpenAI launches GPT-5 model today"], [], 0.88) is True


def test_not_duplicate():
    item = _make_source(title="NVIDIA releases new chip")
    assert _is_duplicate_of_previous(item, set(), ["OpenAI launches GPT-5"], [], 0.88) is False

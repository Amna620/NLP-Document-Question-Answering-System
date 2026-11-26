from app import split_text_into_chunks

def test_chunks_overlap():
    words = [f"w{i}" for i in range(300)]
    chunks = split_text_into_chunks(" ".join(words))
    assert len(chunks) == 3
    assert chunks[0].split()[-30:] == chunks[1].split()[:30]

def test_empty_text():
    assert split_text_into_chunks("") == []

from queuesmith import FairQueue


def test_oldest_first():
    q = FairQueue()
    q.push("a")
    q.push("b")
    assert q.pop() == "a"
    assert len(q) == 1

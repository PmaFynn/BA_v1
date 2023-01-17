from main import main

#siehe handy notizen "more notes" for ideas to make that work
def test_1400x1050():
        assert main(1400, 1050) == True

def test_1920x1080():
        assert main(1920, 1080) == True

def test_828x1792():
        assert main(828, 1792) == True

def test_1280x800():
        assert main(1280, 800) == True


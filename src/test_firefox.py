from mainFirefox import mainFirefox

def test_firefox_1400x1050():
        assert mainFirefox(1400, 1050) == True

def test_firefox_1920x1080():
        assert mainFirefox(1920, 1080) == True

def test_firefox_828x1792():
        assert mainFirefox(828, 1792) == True

def test_firefox_1280x800():
        assert mainFirefox(1280, 800) == True
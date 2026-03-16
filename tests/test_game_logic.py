from logic_utils import check_guess, parse_guess

# Tests for original functionality
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# NEW TESTS FOR BUG FIX #1: Range Validation
def test_parse_guess_rejects_negative_numbers():
    """Bug Fix #1: Negative numbers should be rejected"""
    ok, guess_int, err = parse_guess("-34", low=1, high=100)
    assert ok == False
    assert guess_int is None
    assert "between 1 and 100" in err

def test_parse_guess_rejects_numbers_over_100():
    """Bug Fix #1: Numbers over 100 should be rejected in Normal difficulty"""
    ok, guess_int, err = parse_guess("150", low=1, high=100)
    assert ok == False
    assert guess_int is None
    assert "between 1 and 100" in err

def test_parse_guess_accepts_valid_numbers():
    """Bug Fix #1: Numbers within range should be accepted"""
    ok, guess_int, err = parse_guess("50", low=1, high=100)
    assert ok == True
    assert guess_int == 50
    assert err is None

def test_parse_guess_accepts_boundary_values():
    """Bug Fix #1: Boundary values (1 and 100) should be accepted"""
    # Test lower boundary
    ok, guess_int, err = parse_guess("1", low=1, high=100)
    assert ok == True
    assert guess_int == 1
    
    # Test upper boundary
    ok, guess_int, err = parse_guess("100", low=1, high=100)
    assert ok == True
    assert guess_int == 100

def test_parse_guess_with_easy_difficulty_range():
    """Bug Fix #1: Range validation should work for Easy difficulty (1-20)"""
    # Valid in Easy range
    ok, guess_int, err = parse_guess("15", low=1, high=20)
    assert ok == True
    assert guess_int == 15
    
    # Invalid in Easy range (21 > 20)
    ok, guess_int, err = parse_guess("21", low=1, high=20)
    assert ok == False
    assert "between 1 and 20" in err

# NEW TESTS FOR BUG FIX #2: Corrected Hint Messages
def test_check_guess_correct_high_hint_message():
    """Bug Fix #2: When guess > secret, should say 'Go LOWER!' not 'Go HIGHER!'"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_check_guess_correct_low_hint_message():
    """Bug Fix #2: When guess < secret, should say 'Go HIGHER!' not 'Go LOWER!'"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_check_guess_message_consistency():
    """Bug Fix #2: All "Too High" results should say 'Go LOWER!' """
    test_cases = [
        (100, 50),
        (75, 50),
        (51, 50),
    ]
    for guess, secret in test_cases:
        outcome, message = check_guess(guess, secret)
        assert outcome == "Too High"
        assert "LOWER" in message, f"Failed for guess={guess}, secret={secret}, message={message}"

def test_check_guess_message_consistency_low():
    """Bug Fix #2: All "Too Low" results should say 'Go HIGHER!' """
    test_cases = [
        (1, 50),
        (25, 50),
        (49, 50),
    ]
    for guess, secret in test_cases:
        outcome, message = check_guess(guess, secret)
        assert outcome == "Too Low"
        assert "HIGHER" in message, f"Failed for guess={guess}, secret={secret}, message={message}"


import q1

source = ("name", ["nick1", "nick2"], "2000-01-01", {
    "street": "street",
    "city": "city",
    "prov": "prov",
    "postcode": "postcode"
})


def test_deep_copy_is_not_same_object():
  assert q1.deep_copy(
      source
  ) is not source, "deep_copy should return a new tuple but yours returns the same tuple"


def test_deep_copy_is_deep():
  copy = q1.deep_copy(source)
  assert copy[1] is not source[
      1], "deep_copy should copy the nickname list data, but yours simply copies the list reference"
  assert copy[3] is not source[
      3], "deep_copy should copy the nickname list data, but yours simply copies the list reference"


def test_deep_copy_is_same_value():
  copy = q1.deep_copy(source)
  assert copy == source, "deep_copy should return a copy containing the same values, but yours has different values"

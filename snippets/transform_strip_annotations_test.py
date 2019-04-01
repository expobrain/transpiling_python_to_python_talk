import ast

import pytest
import astor

from transform_strip_annotations import StripAnnotationsTransformer


@pytest.mark.parametrize(
    "source, expected",
    [
        # Assignments
        ("a = 42", "a = 42"),  # no-op
        ("a, b = 1, 2", "a, b = 1, 2"),  # no-op
        ("a: int = 42", "a = 42"),
    ],
)
def test_remove_annotations(source, expected):
    source_ast = ast.parse(source)

    StripAnnotationsTransformer(source_ast)

    result = astor.to_source(source_ast)
    expected_gen = astor.to_source(ast.parse(expected))

    assert result == expected_gen

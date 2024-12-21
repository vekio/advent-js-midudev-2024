from challenge15 import draw_table


def test_draw_table1():
    assert (
        draw_table(
            [
                {"name": "Alice", "city": "London"},
                {"name": "Bob", "city": "Paris"},
            ]
        )
        == """+-------+--------+
| Name  | City   |
+-------+--------+
| Alice | London |
| Bob   | Paris  |
+-------+--------+"""
    )


def test_draw_table2():
    assert (
        draw_table(
            [
                {"name": "Alice", "city": "London"},
            ]
        )
        == """+-------+--------+
| Name  | City   |
+-------+--------+
| Alice | London |
+-------+--------+"""
    )


def test_draw_table3():
    assert (
        draw_table(
            [
                {"gift": "Doll", "quantity": 10},
                {"gift": "Book", "quantity": 5},
                {"gift": "Music CD", "quantity": 1},
            ]
        )
        == """+----------+----------+
| Gift     | Quantity |
+----------+----------+
| Doll     | 10       |
| Book     | 5        |
| Music CD | 1        |
+----------+----------+"""
    )


def test_draw_table4():
    assert (
        draw_table(
            [
                {"gift": "Doll"},
                {"gift": "Book"},
            ]
        )
        == """+------+
| Gift |
+------+
| Doll |
| Book |
+------+"""
    )

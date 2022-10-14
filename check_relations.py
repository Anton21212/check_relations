from typing import Tuple


def check_relation(net: Tuple[Tuple, ...], first: str, second: str) -> bool:
    friends_mapping = __get_friends_mapping(net=net)
    if not (first in friends_mapping and second in friends_mapping):
        return False
    result = __check_relation_recursive(
        friends_mapping=friends_mapping,
        first=first,
        second=second,
        verified_names=[]
    )
    return result


def __get_friends_mapping(net: Tuple[Tuple, ...]) -> dict:
    friends_mapping = {}
    for first, second in net:
        if first not in friends_mapping:
            friends_mapping[first] = []
        if second not in friends_mapping:
            friends_mapping[second] = []
        friends_mapping[first].append(second)
        friends_mapping[second].append(first)
    return friends_mapping


def __check_relation_recursive(
        friends_mapping: dict,
        first: str,
        second: str,
        verified_names: list
) -> bool:
    friends = friends_mapping[first]
    verified_names.append(first)
    for friend in friends:
        if friend in verified_names:
            continue
        if friend == second:
            return True
        checking_result = __check_relation_recursive(
            friends_mapping=friends_mapping,
            first=friend,
            second=second,
            verified_names=verified_names
        )
        if checking_result:
            return True
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Степа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша"),
    )

    assert check_relation(net, "Петя", "Степа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Степа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True

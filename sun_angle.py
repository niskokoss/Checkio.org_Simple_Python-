# Ваша задача - определить угол солнца над горизонтом, зная время суток.
# Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов.
# В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов.
# В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".



from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    x = time.split(":")
    minute = int(x[0]) * 60 + int(x[1])
    return (minute - 360) * 0.25 if 360 <= minute <= 1080 else "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

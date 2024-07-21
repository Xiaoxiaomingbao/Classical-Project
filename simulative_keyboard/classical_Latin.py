import pyperclip
import keyboard

macron_dict = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū', 'y': 'ȳ', 'A': 'Ā', 'E': 'Ē', 'I': 'Ī', 'O': 'Ō',
               'U': 'Ū', 'Y': 'Ȳ', 'æ': 'ǣ', 'Æ': 'Ǣ'}
ligature_dict = {'a': 'æ', 'o': 'œ', 'A': 'Æ', 'O': 'Œ'}
# 注：上面也包括了一些拉丁语用不到的字符
# 若既有ligature又有macron，macron是最后一步


def on_key_event(e):
    global last_char
    # 检查事件是否为按键事件
    if e.event_type == keyboard.KEY_DOWN:
        if len(e.name) == 1 and 'a' <= e.name <= 'z':
            if e.name == 'e':
                add_ligature()
            else:
                last_char = e.name
        elif len(e.name) == 1 and 'A' <= e.name <= 'Z':
            last_char = e.name
        elif e.name == '/':
            add_macron()
        else:
            last_char = ' '


def add_macron():
    global last_char
    global macron_dict
    if last_char not in list(macron_dict.keys()):
        last_char = ' '
        return 0
    # 将字符复制到剪贴板
    text = macron_dict[last_char]
    last_char = text
    pyperclip.copy(text)
    # 模拟删除和粘贴操作
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('ctrl+v')


def add_ligature():
    global last_char
    global ligature_dict
    if last_char not in list(ligature_dict.keys()):
        last_char = 'e'
        return 0
    # 将字符复制到剪贴板
    text = ligature_dict[last_char]
    last_char = text
    pyperclip.copy(text)
    # 模拟删除和粘贴操作
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('ctrl+v')


# 控制和调用last_character是关键
last_char = ''
print('拉丁语键盘已启动！')

# 绑定监听器到按键事件
keyboard.hook(on_key_event)

# 阻塞程序，等待按键事件
keyboard.wait('esc')

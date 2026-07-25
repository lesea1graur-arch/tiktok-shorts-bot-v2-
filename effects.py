"""
effects.py — стили, цвета, подсветка ключевых слов, утилиты для субтитров
"""

HIGHLIGHT_WORDS = {
    'fomo', 'убивает', 'пике', 'верху', 'разворачивается', 'забирает',
    'плечо', 'ликвидация', 'стоп', 'убыток', 'прибыль', 'дисциплина',
    'эмоции', 'деньги', 'депозит', 'рынок', 'трейдер', 'крипта', 'биткоин',
    'памп', 'дамп', 'лонг', 'шорт', 'маржа', 'фьючерс', 'тейк', 'профит',
    'план', 'стратегия', 'риск', 'упустить', 'опоздавших', 'раньше',
    'заработали', 'зашёл', 'вошёл', 'вход', 'вошел', 'слив',
    'паника', 'жадность', 'страх', 'киты', 'тренд', 'коррекция',
    'инфляция', 'подушка', 'кредит', 'долг', 'пассивный', 'доход'
}

COLOR_WHITE = (255, 255, 255)
COLOR_GOLD = (255, 215, 0)
COLOR_GRAY = (140, 140, 140)


def get_word_color(word, is_active):
    w = word.lower().strip('.,!?;:"')
    if is_active and w in HIGHLIGHT_WORDS:
        return COLOR_GOLD
    elif is_active:
        return COLOR_WHITE
    else:
        return COLOR_GRAY


def get_hook_color(text):
    t = text.lower()
    danger = ['fomo', 'убивает', 'слив', 'потеря', 'убыток', 'ликвидация',
              'паника', 'страх', 'долг', 'кредит', 'азарт']
    success = ['прибыль', 'заработок', 'план', 'стратегия', 'выигрыш',
               'профит', 'тейк', 'подушка']

    if any(w in t for w in danger):
        return (255, 60, 60)
    if any(w in t for w in success):
        return (0, 230, 120)
    return (255, 200, 0)


def split_words_into_lines(words, font, draw, max_width, spacing=20):
    """Перенос слов на новые строки по ширине экрана"""
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        bbox = draw.textbbox((0, 0), word, font=font)
        word_w = bbox[2] - bbox[0]

        if current_width + word_w + (spacing if current_line else 0) > max_width and current_line:
            lines.append(current_line)
            current_line = [word]
            current_width = word_w
        else:
            current_line.append(word)
            current_width += word_w + (spacing if len(current_line) > 1 else 0)

    if current_line:
        lines.append(current_line)

    return lines


def calculate_line_width(line_words, font, draw, spacing=20):
    """Ширина строки в пикселях"""
    total = 0
    for i, word in enumerate(line_words):
        bbox = draw.textbbox((0, 0), word, font=font)
        total += (bbox[2] - bbox[0])
        if i < len(line_words) - 1:
            total += spacing
    return total

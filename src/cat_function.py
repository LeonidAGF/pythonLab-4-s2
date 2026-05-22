def cat(path: str) -> str:
    """
    функция реализующая команду cat, которая возвращает текст из файла
    """
    try:
        file = open(path, 'r')
        file_text = file.read()
        file.close()
        return file_text
    except Exception:
        return 'error'

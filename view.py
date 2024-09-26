import webview

def run_window() -> None:
    webview.create_window('Autonomor', 'index.html', False)
    webview.start(gui='qt')


if __name__ == '__main__':
    run_window()

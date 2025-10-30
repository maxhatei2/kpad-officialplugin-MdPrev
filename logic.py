def action(editor):
    parent = editor._appinstance
    editor.prepare_for_external_libs()
    import markdown # type: ignore
    import tkhtmlview # type: ignore
    import customtkinter # type: ignore
    from tkinter import font as tkfont
    text = editor.get_text_from_box()
    html = markdown.markdown(text)

    display_frame = editor.Widget_Frame(parent)
    preview_frame = editor.Widget_Other(display_frame, tkhtmlview.HTMLLabel, html=html, background="white")

    display_frame.pack(side=customtkinter.RIGHT, fill='both', expand=True)
    preview_frame.pack(fill='both', expand=True)

    def refresh(event=None):
        text = editor.get_text_from_box()
        html = markdown.markdown(text)
        preview_frame.set_html(html)
    
    editor.bind('<KeyRelease>', refresh)

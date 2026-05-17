default persistent.sleepover_chinese_enabled = True

init -2 python:
    _sleepover_chinese_font = "fonts/LXGWWenKaiTC-Regular.ttf"

    if persistent.sleepover_chinese_enabled:
        config.language = "chinese"
        config.default_language = "chinese"
    
    gui.language = "unicode"
    
    def _sleepover_chinese_patch_force_language():
        if persistent.sleepover_chinese_enabled:
            _preferences.language = "chinese"
            renpy.change_language("chinese", force=True)
        else:
            _preferences.language = None
            renpy.change_language(None, force=True)

    config.start_callbacks.append(_sleepover_chinese_patch_force_language)
    config.after_load_callbacks.append(_sleepover_chinese_patch_force_language)

    def _sleepover_toggle_language():
        persistent.sleepover_chinese_enabled = not persistent.sleepover_chinese_enabled
        _sleepover_chinese_patch_force_language()
        renpy.restart_interaction()
        if persistent.sleepover_chinese_enabled:
            renpy.notify("已切换至中文 / Switched to Chinese")
        else:
            renpy.notify("已切换至英文 / Switched to English")

    # Add a keybinding to toggle language (Shift+L)
    config.underlay.append(renpy.Keymap(shift_K_l=_sleepover_toggle_language))

init 999 python:
    # Always set font for key styles to support Chinese characters,
    # as the Chinese font also supports English perfectly.
    # This prevents "garbled" text (tofu blocks) when switching or in specific UI elements.
    
    def _sleepover_apply_global_fonts():
        _sleepover_chinese_font = "fonts/LXGWWenKaiTC-Regular.ttf"

        def _sleepover_set_style_font(style_name):
            try:
                getattr(style, style_name).font = _sleepover_chinese_font
            except Exception:
                pass

        for _style_name in (
            "default",
            "say_dialogue",
            "say_label",
            "button_text",
            "input",
            "choice_button_text",
            "choice_button_text1",
            "choice_button_text1_hovered",
            "choice_button_text2",
            "choice_button_text2_hovered",
            "choice_button_text3",
            "choice_button_text3_hovered",
            "choice_button_text4",
            "choice_button_text4_hovered",
            "sex_choice_L_text",
            "sex_choice_L_text_hovered",
            "sex_choice_M_text",
            "sex_choice_M_text_hovered",
            "sex_choice_S_text",
            "sex_choice_S_text_hovered",
            "quick_button_text",
            "readback_text",
            "nvl_dialogue",
            "nvl_label",
            "nvl_thought",
        ):
            _sleepover_set_style_font(_style_name)

    _sleepover_apply_global_fonts()

# Use Ren'Py's style translation system for better compatibility with language switching
translate chinese style default:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style say_dialogue:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style say_label:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style button_text:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style choice_button_text:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style choice_button_text1:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style choice_button_text2:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style choice_button_text3:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style choice_button_text4:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style sex_choice_L_text:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style sex_choice_M_text:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese style sex_choice_S_text:
    font "fonts/LXGWWenKaiTC-Regular.ttf"

translate chinese python:
    _sleepover_chinese_font = "fonts/LXGWWenKaiTC-Regular.ttf"
    gui.text_font = _sleepover_chinese_font
    gui.name_text_font = _sleepover_chinese_font
    gui.interface_text_font = _sleepover_chinese_font
    gui.button_text_font = _sleepover_chinese_font
    gui.choice_button_text_font = _sleepover_chinese_font
    gui.language = "unicode"

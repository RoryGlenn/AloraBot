from . import colorscheme

app_bg = f"""background: {colorscheme.bg_color};
        border-radius: 15px"""

log_bg = f"""background: {colorscheme.bg_log};
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 15px;"""

title_bar_detail = f"""background: {colorscheme.bg_log};
        border-top-left-radius: 0px;
        border-top-right-radius: 15px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;"""

title_bar = f"""background: {colorscheme.transparent}"""

logo_text = f"""color: {colorscheme.text_color}"""

info_widget = f"""background: {colorscheme.log_aux_color};
                border-radius: 8px"""

info_widget_labels = f"""background: {colorscheme.transparent};
                    color: {colorscheme.text_color}"""

link_entry = f"""background: {colorscheme.second_color};
            border-radius: 8px"""

cfg_container = f"""background: {colorscheme.second_color};
            border-radius: 8px"""

start_btn_default = f"""background: {colorscheme.seledyn_color};
                        color: {colorscheme.bg_color};
                        border-radius: 8px"""

stop_btn_default = f"""background: {colorscheme.red_color};
                        color: {colorscheme.bg_color};
                        border-radius: 8px"""

log_container = f"""background: {colorscheme.second_color}"""

scroll_area = f"""QScrollBar:vertical{{background: rgba(0, 0, 0, 0);
                                    width:8px;
                                    }}
                                    QScrollBar:horizontal{{background: rgba(0, 0, 0, 0);
                                    height:8px;
                                    }}
                                    QScrollBar::handle:vertical {{
                                    background-color: {colorscheme.log_aux_color};
                                    min-height: 20px;
                                    margin: 0px;
                                    border-radius: 4px;;
                                    }}
                                    QScrollBar::handle:horizontal {{
                                    background-color: {colorscheme.log_aux_color};
                                    min-width: 20px;
                                    margin: 0px;
                                    border-radius: 4px;;
                                    }}
                                    QScrollBar::add-line, QScrollBar::sub-line {{
                                    border: none;
                                    background: none;
                                    }}
                                    QScrollBar::up-arrow, QScrollBar::down-arrow, 
                                    QScrollBar::add-page, QScrollBar::sub-page {{
                                    border: none;
                                    background: none;
                                    color: none;}}"""

transparent = f"""background: {colorscheme.transparent}"""

log_success = f"""background: {colorscheme.green_color};
                border-radius: 2px"""

log_error = f"""background: {colorscheme.red_color};
                border-radius: 2px"""

log_aux = f"""background: {colorscheme.log_aux_color};
                border-radius: 2px"""

log_widget = f"""background: {colorscheme.log_aux_color};
                border-radius: 8px"""

reset_style = f"""background: {colorscheme.transparent};
                border-radius: 0px"""

btn_skill = f"""QToolButton{{background: {colorscheme.log_aux_color};
                border-radius: 8px}}
                QToolButton:pressed{{background: {colorscheme.log_aux_color_clicked}}}"""

step_combo = f"""QComboBox {{
                color: #FFFFFF;
                border-radius: 4px;
                padding: 1px 18px 1px 14px;
                background: {colorscheme.log_aux_color};
                        }}

                QComboBox:editable {{
                background: {colorscheme.log_aux_color};
                }}
                
                QComboBox:on {{
                padding-top: 3px;
                padding-bottom: 3px;
                padding-left: 4px;
                }}

                /*QComboBox::down-arrow {{
                        image: url(:/images/Vector.png);
                        }}*/

                QComboBox::down-arrow:on {{
                        top: 1px;
                        left: 1px;}}
                """

mouse_btn = f"""QPushButton{{background: {colorscheme.transparent};
                        color: {colorscheme.text_color}}}
                QPushButton:pressed{{color: #C1BCBC}}"""

bot_popup = f"""background-color: #2e2d32;
                border: none;
                border-radius: 8px"""

bot_popup_circle = f"""background-color: #2e2d32;
                    border: none;
                    border-radius: 10px"""

bot_popup_btn = f"""QPushButton{{background-color: {colorscheme.transparent};
                    border: none;
                    border-radius: 10px;
                    color: {colorscheme.text_color}
                }}
                QPushButton::hover{{ 
                    background-color: {colorscheme.log_aux_color_clicked}
                }}
                """

default_btn = f"""QPushButton{{background: {colorscheme.seledyn_color};
                        color: {colorscheme.bg_color};
                        border-radius: 5px;}}
                """

entry_seconds_spend = f"""background: {colorscheme.log_aux_color};
                        border-radius: 8px;
                        padding-left: 8px;
                        padding-right: 8px;
                        color: {colorscheme.text_color}"""

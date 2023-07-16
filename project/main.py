from flet import *
import pygame

def main(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER

    #txt_number = TextField(value="0", text_align=TextAlign.RIGHT, width=100)
    volume_slider = Slider()
    # Pick files dialog
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )

        selected_files.update()
    
    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()


    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog])


    # play open file
    def play(e):
        global played
        #txt_number.value = selected_files.value
        #page.update()
        pygame.mixer.init()
        pygame.mixer.music.load(selected_files.value)
        pygame.mixer.music.play()
        played= True

   # pause the music
    def pause(e):
        global played
        if played == False:
            #txt_number.value = selected_files.value
            #page.update()
            pygame.mixer.music.unpause()
            played = True
        else:
            #txt_number.value = "Pause"
            #page.update()
            pygame.mixer.music.pause()
            played = False

    # chanch volume
    def volume(e):
        v = 0.01 * e.control.value    
        pygame.mixer.music.set_volume(v)

    page.add(
        Row(
            [
                #txt_number,
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
                IconButton(icons.PLAY_ARROW, on_click=play),
                IconButton(icons.PAUSE, on_click=pause),
                Slider(min=0, max=100, divisions=100, value=100, label="{value}%", on_change=volume),          
            ],
            alignment=MainAxisAlignment.CENTER,
            
        ),
    )


if __name__ == "__main__":
    app(target=main)

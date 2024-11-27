import flet as fl


def main(page: fl.Page):
    page.title = "Login"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window.width = 500

    txt_username = fl.TextField(
        icon=fl.icons.PERSON, label="Username")
    txt_password = fl.TextField(
        icon=fl.icons.SECURITY_ROUNDED, password=True, label="Password")

    def handle_change(e):
        if txt_username.value and txt_password.value:
            page.add(fl.Text(f"Hi {txt_username.value}"))
        else:
            page.add(fl.Text("Required and Password and/or Username"))
        page.update()

    button_submit = fl.ElevatedButton(
        text="Submit", on_click=handle_change)

    page.add(
        txt_username,
        txt_password,
        button_submit
    )


if __name__ == '__main__':
    fl.app(main)

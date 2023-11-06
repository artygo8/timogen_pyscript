from pyscript import Element


def therapist_name_change():
    def get_button(name):
        return f'<button class="dropdown-item" type="button" py-click="therapist_name_click(\'{name}\')">{name}</button>'

    name_input = Element("therapist_name")
    available_names = Element("available_therapist_names")
    if therapists:
        value = name_input.element.value.lower()
        if value:
            therapist_names = [
                therapist["name"]
                for therapist in therapists
                if therapist["name"].lower().startswith(value)
                and therapist["name"].lower() != value
            ]
        else:
            therapist_names = []

        available_names.element.hidden = False if therapist_names else True
        therapist_names.sort()
        available_names.element.innerHTML = "".join(
            [get_button(name) for name in therapist_names]
        )


def therapist_name_click(name):
    name_input = Element("therapist_name")
    name_input.element.value = name
    therapist_name_change()
    therapist = next(
        (
            therapist
            for therapist in therapists
            if therapist["name"].lower() == name.lower()
        ),
        None,
    )
    if therapist:
        Element("therapist_address").element.value = therapist.get("address", '')
        Element("therapist_inami").element.value = therapist.get("inami_nb", '')
        Element("therapist_bce").element.value = therapist.get("bce", '')
        Element("contracted").element.checked = therapist.get("contracted", False)

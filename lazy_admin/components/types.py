# -*- coding: utf-8 -*-


from enum import StrEnum


class ComponentTypes(StrEnum):
    """Component types."""

    button = "button"
    checkbox = "checkbox"
    color = "color"
    date = "date"
    datetime_local = "datetime-local"
    email = "email"
    file = "file"
    hidden = "hidden"
    image = "image"
    month = "month"
    number = "number"
    password = "password"
    radio = "radio"
    range = "range"
    reset = "reset"
    search = "search"
    submit = "submit"
    tel = "tel"
    text = "text"
    time = "time"
    url = "url"
    week = "week"

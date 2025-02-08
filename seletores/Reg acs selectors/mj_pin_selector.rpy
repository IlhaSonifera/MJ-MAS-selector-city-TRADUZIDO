# Credit to RaVen for a template, submod by MayJay

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["pin_acs"] = {
        "_ev": "mj_pin_acs_select",
        "_min-items": 1,
        "change": "Pode mudar seu pin?",
        "wear": "Você pode usar um pin?",
    }

#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_pin_acs_select",
            category=["aparência"],
            prompt=store.mas_selspr.get_prompt("pin_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_pin_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="pin_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("Que tipo de pin eu deveria usar?")
        sel_map = {}

    m 1eua "Claro [player]!"

    call mas_selector_sidebar_select_acs(use_acs, [mas_quipExp('6eua')], mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Ah, tudo bem."

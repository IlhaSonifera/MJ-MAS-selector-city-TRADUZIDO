# Credit to RaVen / ATOMreal for a template, submod by mayday-mayjay (dont reupload my stuff, nerd)

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["cushion_acs"] = {
        "_ev": "mj__cushion_acs_select",
        "_min-items": 1,
        "change": "Pode usar uma almofada diferente?",
        "wear": "Você quer descansar seus braços em uma almofada?",
    }

#init -9 python in mas_selspr:
    #GRP_TOPIC_LIST.append("ahoge_acs")


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj__cushion_acs_select",
            category=["mesa"],
            prompt=store.mas_selspr.get_prompt("cushion_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj__cushion_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="cushion_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("Uma boa almofada é um cotovelo relaxado!")
        sel_map = {}

    m 1eua "Claro [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Ah, tudo bem."

# Credit to RaVen / ATOM_real for a template, submod by MayJay (dont reupload my stuff, nerd)

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["ear_acs"] = {
        "_ev": "mj_ear_acs_select",
        "_min-items": 1,
        "change": "Pode mudar seu acessório de orelha?",
        "wear": "Você pode usar um acessório de orelha?",
    }

#init -9 python in mas_selspr:
    #GRP_TOPIC_LIST.append("ahoge_acs")


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_ear_acs_select",
            category=["aparência"],
            prompt=store.mas_selspr.get_prompt("ear_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_ear_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="ear_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("Qual acessório de orelha eu deveria usar?")
        sel_map = {}

    m 1eua "Claro [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Ah, tudo bem."
#créditos para my-otter-self / your-otter-friend por ajudar com o repo, créditos ao raVen e (sigh) ATOM_real pelo código de seletor original para base.

init -990 python in mas_submod_utils:
    Submod(
        author="MayJay",
        name="Selector City",
        description="Uma coleção de seletores mantida por u/mayday-mayjay em uma área em ordem para utilizar o atualizador de submod. Por favor reporte um problema no repositório, ou vá para o servidor de trabalho de submods: https://discord.gg/Tx23rczN8N. Em caso de problemas com a tradução: https://discord.gg/bMPDaCVz",
        version="1.0.3",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Selector City",
            user_name="mayday-mayjay",
            repository_name="MJ-MAS-selector-city",
            submod_dir="/Submods/Selector City",
            extraction_depth=3,
            redirected_files=(
                "README.md"
            )
        )

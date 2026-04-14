def select_agents(user_input, agents):
    selected = []

    for agent in agents:
        if agent.can_handle(user_input):
            selected.append(agent)

    if not selected:
        selected = agents  # fallback

    return selected

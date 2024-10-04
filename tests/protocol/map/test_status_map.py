from aiwolf_nlp_common.protocol.map.status_map import StatusMap, Status, AgentStatus


def test_set_received_info(initialize_json:dict, status_map_json:dict) -> None:
    test_map = StatusMap()
    test_map.set_received_info(set_map=initialize_json["gameInfo"]["statusMap"])

    check_set:set[AgentStatus] = set()
    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"
        add_elem = AgentStatus(agent=name, status="ALIVE")
        check_set.add(add_elem)

    assert test_map == check_set

    test_map.set_received_info(set_map=status_map_json["gameInfo"]["statusMap"])
    check_set.clear()

    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"

        if i+1 != 1 and i+1 != 2 and i+1 != 3:
            check_set.add(AgentStatus(agent=name, status="ALIVE"))
        else:
            check_set.add(AgentStatus(agent=name, status="DEAD"))

    assert test_map == check_set

def test_set_alive() -> None:

    test_map = StatusMap()

    check_set:set[AgentStatus] = set()
    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"

        test_map.set_alive(agent=name)
        add_elem = AgentStatus(agent=name, status="ALIVE")
        check_set.add(add_elem)

    assert test_map == check_set

def test_set_dead() -> None:
    test_map = StatusMap()

    check_set:set[AgentStatus] = set()

    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"

        if i+1 != 1 and i+1 != 2 and i+1 != 3:
            check_set.add(AgentStatus(agent=name, status="ALIVE"))
            test_map.set_alive(agent=name)
        else:
            check_set.add(AgentStatus(agent=name, status="DEAD"))
            test_map.set_dead(agent=name)

    assert test_map == check_set

def test_set_reverse_status() -> None:
    test_map = StatusMap()

    check_set:set[AgentStatus] = set()

    for i in range(5):
        name = "Agent[0" + str(i+1) + "]"

        if i+1 != 1 and i+1 != 2 and i+1 != 3:
            check_set.add(AgentStatus(agent=name, status="ALIVE"))
            test_map.set_dead(agent=name)
        else:
            check_set.add(AgentStatus(agent=name, status="DEAD"))
            test_map.set_alive(agent=name)
        
        test_map.reverse_status(agent=name)

    assert test_map == check_set
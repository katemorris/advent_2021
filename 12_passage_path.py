from unicodedata import name
import pprint
import code


def read_connections(file):
    open_file = open(file, "r")
    lines = open_file.read().splitlines()
    return lines


def cave_type(cave_name):
    lower_cave_name = cave_name.lower()
    if cave_name == lower_cave_name:
        return "small"
    else:
        return "big"


def make_cave_map(lines):
    caves = {}
    for line in lines:
        caves_set = line.split("-")
        cave1 = caves_set[0]
        cave2 = caves_set[1]
        if cave1 not in caves.keys():
            caves[cave1] = {"type": cave_type(cave1), "connected_to": {cave2}}
        else:
            caves[cave1]["connected_to"].add(cave2)

        if cave2 not in caves.keys():
            caves[cave2] = {"type": cave_type(cave2), "connected_to": {cave1}}
        else:
            caves[cave2]["connected_to"].add(cave1)
    # clear end
    caves["end"]["connected_to"] = {}
    # remove start
    for data in caves.values():
        if "start" in data["connected_to"]:
            data["connected_to"].remove("start")
    return caves


def traverse_caves(
    current_cave_key, caves, paths=[], current_path=[], ignored_caves=[]
):
    print(f"top of method current cave: {current_cave_key}")

    while current_cave_key:
        connected_caves = list(caves[current_cave_key]["connected_to"])
        temp_ignored = []
        if current_cave_key != "end" and set(connected_caves).issubset(
            set(ignored_caves)
        ):
            remove_last = current_path.pop()
            if remove_last in ignored_caves:
                ignored_caves.remove(remove_last)
            if caves[remove_last]["type"] == "big":
                temp_ignored.append(remove_last)
            print(f"No more caves in {current_cave_key} ... breaking in top loop")
            code.interact(local=dict(globals(), **locals()))
            break
        elif current_cave_key != "end":
            if current_cave_key == "start":
                current_path.append(current_cave_key)
            for index, cave in enumerate(connected_caves):

                if cave not in ignored_caves and cave not in temp_ignored:
                    if current_path[-1] == cave:
                        continue
                    else:
                        current_path.append(cave)
                    print(f"{cave} added to the path, digging")
                    code.interact(local=dict(globals(), **locals()))
                    if caves[cave]["type"] == "small" and cave != "end":
                        ignored_caves.append(cave)
                    print(f"current path: {current_path}")
                    print(f"ignored caves: {ignored_caves}")
                    print(f"currrent cave: {current_cave_key}")
                    print(f"next cave: {cave}")
                    code.interact(local=dict(globals(), **locals()))
                    traverse_caves(cave, caves, paths, current_path, ignored_caves)
                elif (cave in ignored_caves or cave in temp_ignored) and index == (
                    len(connected_caves) - 1
                ):
                    remove_last = current_path.pop()
                    if remove_last in ignored_caves:
                        ignored_caves.remove(remove_last)
                    if caves[remove_last]["type"] == "big":
                        temp_ignored.append(remove_last)
                    print(
                        f"No more caves in {current_cave_key} ... breaking in smallest loop"
                    )
                    code.interact(local=dict(globals(), **locals()))
                    continue
                else:
                    print(
                        f"Checking next cave with index {index+1} of {len(connected_caves)} in {current_cave_key} as {cave} as been ignored"
                    )
                    code.interact(local=dict(globals(), **locals()))
                    continue
        elif current_cave_key == "end":
            # current_path.append(current_cave_key)
            if current_path in paths:
                current_path.pop()
                remove_last = current_path.pop()
                if remove_last in ignored_caves:
                    ignored_caves.remove(remove_last)
                break
            else:
                paths.append(current_path.copy())
                current_path.pop()
                print(f"paths are: {paths}")
                print(f"Going back to path {current_path}")
                break

    return paths


lines = read_connections("files/day12.txt")
caves = make_cave_map(lines)
pprint.pprint(caves)
completed_paths = traverse_caves("start", caves)
print(completed_paths)
# return len(completed_paths)

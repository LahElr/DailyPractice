from typing import Any, Iterable, List, Union
from bidict import bidict


class InvariantDict:
    def __init__(self, len=0):
        self.len = len

    def __getitem__(self, key):
        return key

    def __len__(self):
        return self.len


class Graph:
    def __init__(
        self, arg: Union[Iterable[Iterable[Any]], int], default_val=1, directional=True
    ):
        self.default_val = default_val
        self.directional = directional
        if isinstance(arg, int):
            node_count = arg
            self.matrix = [[0 for _ in range(node_count)] for _ in range(node_count)]
            self.node_count = node_count
            self.name_key_bidict = InvariantDict(node_count)
        elif hasattr(arg, "__getitem__") or hasattr(arg, "__iter__"):
            edges = arg
            self.name_key_bidict = bidict()
            node_count = 0
            start_id = 0
            end_id = 0
            edge_ids = []
            for edge in edges:
                try:
                    start_id = self.name_key_bidict[edge[0]]
                except KeyError:
                    self.name_key_bidict[edge[0]] = node_count
                    start_id = node_count
                    node_count += 1

                try:
                    end_id = self.name_key_bidict[edge[1]]
                except KeyError:
                    self.name_key_bidict[edge[1]] = node_count
                    end_id = node_count
                    node_count += 1
                edge_ids.append(
                    [start_id, end_id, edge[2] if len(edge) >= 3 else default_val]
                )

            self.matrix = [[0 for _ in range(node_count)] for _ in range(node_count)]
            self.node_count = node_count

            for edge in edge_ids:
                self.matrix[edge[0]][edge[1]] = edge[2]
                if not self.directional:
                    self.matrix[edge[1], edge[2]] = edge[2]
        else:
            raise ValueError("Not parsable arg", stacklevel=2)

    def set_edge(self, start, end, val=None):
        try:
            self.matrix[self.name_key_bidict[start]][self.name_key_bidict[end]] = (
                val if val is not None else self.default_val
            )
            if not self.directional:
                self.matrix[self.name_key_bidict[end]][self.name_key_bidict[start]] = (
                    val if val is not None else self.default_val
                )
        except KeyError:
            raise ValueError("Not exist node name", stacklevel=2)

    def get_edge(self, start, end):
        try:
            return self.matrix[self.name_key_bidict[start]][self.name_key_bidict[end]]
        except KeyError:
            raise ValueError("Not exist node name", stacklevel=2)

    def get_in_degree(self, node, except_node_list=[]):
        return sum(
            [
                self.matrix[self.name_key_bidict[_]][self.name_key_bidict[node]]
                for _ in self.name_key_bidict.keys()
                if _ not in except_node_list
            ]
        )

    def get_out_degree(self, node, except_node_list=[]):
        return sum(
            [
                self.matrix[self.name_key_bidict[node]][self.name_key_bidict[_]]
                for _ in self.name_key_bidict.keys()
                if _ not in except_node_list
            ]
        )

    def __set_edge(self, start_id, end_id, val=None):
        try:
            self.matrix[start_id][end_id] = val if val is not None else self.default_val
            if not self.directional:
                self.matrix[end_id][start_id] = (
                    val if val is not None else self.default_val
                )
        except IndexError:
            raise ValueError("Not exist node id", stacklevel=2)

    def __get_edge(self, start_id, end_id):
        try:
            return self.matrix[start_id][end_id]
        except IndexError:
            raise ValueError("Not exist node id", stacklevel=2)

    def __get_in_degree(self, node_id, except_node_list=[]):
        try:
            return sum(
                [
                    self.matrix[_][node_id]
                    for _ in range(self.node_count)
                    if _ not in except_node_list
                ]
            )
        except IndexError:
            raise ValueError("Not exist node id", stacklevel=2)

    def __get_out_degree(self, node_id, except_node_list=[]):
        try:
            return sum(
                [
                    self.matrix[node_id][_]
                    for _ in range(self.node_count)
                    if _ not in except_node_list
                ]
            )
        except IndexError:
            raise ValueError("Not exist node id", stacklevel=2)

    def topology_sort(self, return_id=False):
        except_node_list = []
        while True:
            proceeded_flag = False
            for id in range(self.node_count):
                if id not in except_node_list:
                    if self.__get_in_degree(id, except_node_list) == 0:
                        except_node_list.append(id)
                        proceeded_flag = True
            if not proceeded_flag:
                break
        if return_id:
            return except_node_list
        else:
            return [self.name_key_bidict.inv[_] for _ in except_node_list]

    def count_connected_subgraph(
        self,
    ):
        r"""
        连通图计数
        """
        if self.node_count == 1:
            return 1
        graph_count = 0
        nodes_visited = [False for _ in range(self.node_count)]
        for i in range(self.node_count):
            if nodes_visited[i]:
                continue

            # print(f"new node {i}")
            this_graph_stack = [i]
            graph_count += 1
            nodes_visited[i] = True

            while len(this_graph_stack) > 0:
                # print(f"stack:{this_graph_stack}")
                this_node = this_graph_stack.pop(0)
                for candidate_node in range(self.node_count):
                    # 如果超限，自动为空
                    if not nodes_visited[candidate_node] and (
                        self.matrix[this_node][candidate_node] == 1
                        or this_node == candidate_node
                        or self.matrix[candidate_node][this_node]
                    ):
                        nodes_visited[candidate_node] = True
                        this_graph_stack.append(candidate_node)
        return graph_count

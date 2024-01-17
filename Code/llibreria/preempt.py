import queue
import heapq
class Preempt:
    def __init__(self, M):
        self.capacity = M
        self.wait_queue = queue.PriorityQueue()
        self.processing_entities = []  # Heap structure to processing entities by priority
        self.await_file = []  # entities awaiting reactivation

    def request_resource(self, entity_id, priority):
        entity = (-priority, entity_id)

        if len(self.processing_entities) < self.capacity:
            heapq.heappush(self.processing_entities, entity)
            return "Resource seized", None

        lowest_priority_entity = self.processing_entities[0]
        if entity < lowest_priority_entity:
            preempted_entity = heapq.heappop(self.processing_entities)
            self.await_file.append(preempted_entity)
            heapq.heappush(self.processing_entities, entity)
            return "Resource seized with preemption", preempted_entity[1]

        self.wait_queue.put(entity)
        return "Entity waiting", None

    def release_resource(self, entity_id):
        for i, (_, e_id) in enumerate(self.processing_entities):
            if e_id == entity_id:
                heapq.heappop(self.processing_entities, i)
                break

        if self.await_file:
            reactivated_entity = self.await_file.pop(0)
            result, _ = self.request_resource(reactivated_entity[1], -reactivated_entity[0])
            return "Resource released and entity reactivated", reactivated_entity[1]

        if not self.wait_queue.empty() and len(self.processing_entities) < self.capacity:
            next_entity = self.wait_queue.get()
            heapq.heappush(self.processing_entities, next_entity)
            return "Resource released and next entity processed", next_entity[1]

        return "Resource released", None

    def preempt_entity(self, entity_id):
        for i, (priority, e_id) in enumerate(self.processing_entities):
            if e_id == entity_id:
                preempted_entity = heapq.heappop(self.processing_entities, i)
                
                self.await_file.append(preempted_entity)
                

        heapq.heapify(self.processing_entities)

        if not self.wait_queue.empty() and len(self.processing_entities) < self.capacity:
            next_entity = self.wait_queue.get()
            heapq.heappush(self.processing_entities, next_entity)

        return "Entity preempted"

from dfifo import DFifo
import random


class Customer:
    def __init__(self, id, arrival_time, shopping_time, processing_time):
        self.id = id
        self.arrival_time = arrival_time
        self.shopping_time = shopping_time
        self.processing_time = processing_time
        self.queue_entry_time = None
        self.queue_exit_time = None

    def wait_time(self):
        if self.queue_entry_time is not None and self.queue_exit_time is not None:
            return self.queue_exit_time - self.queue_entry_time
        return 0

    def __str__(self):
        return (f"Zakaznik {self.id} (Prichod: {self.arrival_time}, "
                f"Nakupovanie: {self.shopping_time}, Spracovanie: {self.processing_time})")


class Simulation:
    def __init__(self):
        self.p_cislo = 11
        self.customers = []
        # DYNAMICKE FIFO - nahradenie statickeho Fifo(5000) dynamickym DFifo
        self.queue = DFifo()
        self.current_time = 0
        self.next_arrival_time = 0
        self.next_processing_end_time = float('inf')
        self.total_idle_time = 0
        self.max_wait_time = 0
        self.max_queue_length = 0
        self.last_event_time = 0

    def run(self, duration=28800):
        customer_id = 1
        while self.current_time < duration:
            if self.current_time >= self.next_arrival_time:
                shopping_time = 60 * (1 + random.randint(0, 10 + self.p_cislo))
                processing_time = 0.3 * 60 + shopping_time / 20
                customer = Customer(customer_id, self.current_time, shopping_time, processing_time)
                self.customers.append(customer)
                customer_id += 1
                self.next_arrival_time += 5 + random.randint(0, 25 + self.p_cislo)

            if (self.queue.getLength() > 0) and (self.current_time >= self.next_processing_end_time):
                next_customer = self.queue.get()
                next_customer.queue_exit_time = self.current_time
                wait_time = next_customer.wait_time()
                if wait_time > self.max_wait_time:
                    self.max_wait_time = wait_time
                    print(f"  [MAX CAKANIE] {self.max_wait_time / 100:.2f}s")
                print(f"Cas {self.current_time / 100:.2f}s: Zakaznik {next_customer.id} zaplatil, "
                      f"cakal {wait_time / 100:.2f}s | Dlzka radu: {self.queue.getLength()} | "
                      f"Celkova necinnost: {self.total_idle_time / 100:.2f}s")
                if self.queue.getLength() > 0:
                    nxt = self.queue.raw()[0]
                    self.next_processing_end_time = self.current_time + nxt.processing_time
                else:
                    self.next_processing_end_time = float('inf')

            for customer in self.customers:
                if customer.queue_entry_time is None and self.current_time >= customer.arrival_time + customer.shopping_time:
                    customer.queue_entry_time = self.current_time
                    self.queue.put(customer)
                    q_len = self.queue.getLength()
                    print(f"Cas {self.current_time / 100:.2f}s: Zakaznik {customer.id} vstupil do radu | "
                          f"Dlzka radu: {q_len} | Necinnost: {self.total_idle_time / 100:.2f}s")
                    if q_len > self.max_queue_length:
                        self.max_queue_length = q_len
                        print(f"  [MAX RAD] {self.max_queue_length}")
                    if self.next_processing_end_time == float('inf'):
                        self.next_processing_end_time = self.current_time + customer.processing_time

            if self.queue.getLength() == 0:
                idle_duration = self.current_time - self.last_event_time
                if idle_duration > 0:
                    self.total_idle_time += idle_duration
                self.last_event_time = self.current_time

            self.current_time += 1

        print(f"\n=== KONIEC SIMULACIE ===")
        print(f"Celkovy pocet zakaznikov: {len(self.customers)}")
        print(f"Max doba cakania v rade: {self.max_wait_time / 100:.2f}s")
        print(f"Max dlzka radu: {self.max_queue_length}")
        print(f"Celkova necinnost pokladne: {self.total_idle_time / 100:.2f}s")


if __name__ == "__main__":
    sim = Simulation()
    sim.run()

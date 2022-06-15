import unittest
from store import GroceryStore
from simulation import *
import os
import json
from io import StringIO


# with (open("./simulation_result/config2_result.json", 'w')) as f:
#     json.dump(temp, f)


class SimulationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.config_list = list(map (lambda y: "input_files/" + y, (list(filter((lambda x:"json" in x), os.listdir("input_files"))))))
        self.event_list = list(map (lambda y: "input_files/" + y, list(filter((lambda x:"events" in x), (os.listdir("input_files"))))))
        self.simulation_res = list(map(lambda y:"simulation_result/"+y, (list(filter((lambda x:"json" in x), (os.listdir("simulation_result")))))))
        self.simulation_res.sort()
        self.config_list.sort()
        self.event_list.sort()

    def test_1(self):
        config_file = self.config_list[0]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[0])
        sol = json.load(temp, encoding='utf-8')
        filtered_list = [self.event_list[2]] + self.event_list[3:5] + [self.event_list[-1]]
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with "+ config_file)
        temp.close()
        config.close()

    def test_2(self):
        config_file = self.config_list[1]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[1])
        sol = json.load(temp)
        filtered_list = [self.event_list[-3]] + [self.event_list[-1]]
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with "+ config_file)
        config.close()
        temp.close()

    def test_3(self):
        config_file = self.config_list[2]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[2])
        sol = json.load(temp)
        filtered_list = [self.event_list[2]] + self.event_list[3:5] + [self.event_list[-1]]
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            exp = sol[i]
            event_file.close()
            self.assertDictEqual(exp, act, "Fails at " + event + " with "+ config_file)
        temp.close()
        config.close()

    def test_4(self):
        config_file = self.config_list[3]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[3])
        sol = json.load(temp)
        filtered_list = [self.event_list[2]] + self.event_list[3:5] + [self.event_list[-1]]
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            exp = sol[i]
            event_file.close()
            self.assertDictEqual(exp, act, "Fails at " + event + " with "+ config_file)
        config.close()
        temp.close()

    def test_5(self):
        config_file = self.config_list[4]
        config = open(config_file)
        temp = open(self.simulation_res[4])
        sol = json.load(temp)
        store = GroceryStoreSimulation(config)
        filtered_list = self.event_list
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with " + config_file)
        config.close()
        temp.close()

    def test_6(self):
        config_file = self.config_list[5]
        config = open(config_file)
        temp = open(self.simulation_res[5])
        store = GroceryStoreSimulation(config)
        sol = json.load(temp)
        filtered_list = self.event_list
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with " + config_file)
        config.close()
        temp.close()

    def test_7(self):
        config_file = self.config_list[6]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[6])
        sol = json.load(temp)
        filtered_list = self.event_list
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with " + config_file)
        config.close()
        temp.close()

    def test_8(self):
        config_file = self.config_list[7]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[7])
        sol = json.load(temp)
        filtered_list = self.event_list
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with " + config_file)
        config.close()
        temp.close()

    def test_9(self):
        config_file = self.config_list[8]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[8])
        sol = json.load(temp)
        filtered_list = self.event_list
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with " + config_file)
        config.close()
        temp.close()

    def test_10(self):
        config_file = self.config_list[9]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[9])
        sol = json.load(temp)
        filtered_list = self.event_list
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with " + config_file)
        config.close()
        temp.close()

    def test_11(self):
        config_file = self.config_list[10]
        config = open(config_file)
        store = GroceryStoreSimulation(config)
        temp = open(self.simulation_res[10])
        sol = json.load(temp)
        filtered_list = self.event_list
        for i in range(len(filtered_list)):
            event = filtered_list[i]
            event_file = open(event)
            act = store.run(event_file)
            event_file.close()
            exp = sol[i]
            self.assertDictEqual(exp, act, "Fails at " + event + " with " + config_file)
        config.close()
        temp.close()

    def test_12(self):
        CONFIG_FILE = '''{"regular_count": 1,
          "express_count": 0,
          "self_serve_count": 0,
          "line_capacity": 1
        }
        '''
        EVENT_FILE = """17 Arrive Dino a 6
        10 Arrive Tamara Bananas 7
        5 Arrive Jugo Bread 3 Cheese 3"""
        gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
        actual = gss.run(StringIO(EVENT_FILE))
        expected = {"num_customers":3,
                    "max_wait":8,
                    "total_time":24}
        self.assertEqual(expected, actual, "第一个人进来的时候是5s然后第二个人在10s进来但是第一个人直到11s前都无法进来所以要多等1s在11s才能进来然后11s第二个人开始结账一直到18s所以18-10 = 8s这是最大wait才能结束而17s时第三个人进来了所以要多等1s18s开始买单一直到24秒结束")

    def test_13(self):
        CONFIG_FILE = '''{"regular_count": 1,
                  "express_count": 1,
                  "self_serve_count": 1,
                  "line_capacity": 1
                }
                '''
        EVENT_FILE = """23 Arrive Dino a 6
                16 Close 2
                10 Arrive Tamara Bananas 7
                9 Close 1
                5 Arrive Jugo Bread 3 Cheese 3"""
        gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
        actual = gss.run(StringIO(EVENT_FILE))
        expected = {"num_customers": 3,
                    "max_wait": 14,
                    "total_time": 29}
        self.assertEqual(expected, actual,
                         "5s时第一个人进来到11s，而9s时第二条线已经关了，所以10s第二个人进来时必须到self-serve, 第二个人买完单为24s，而16s时第self serve也关了，所以对于23s进来的时候只能去第一条regular它需要的时间是 23 + 6 = 29s")

    def test_14(self):
        CONFIG_FILE = '''{"regular_count": 1,
                  "express_count": 1,
                  "self_serve_count": 0,
                  "line_capacity": 2
                }
                '''
        EVENT_FILE = """10 Arrive Dino a 6
                15 Close 1
                5 Arrive Tamara Bananas 7
                11 Close 0
                2 Arrive Jugo Bread 8 Cheese 2"""
        gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
        actual = gss.run(StringIO(EVENT_FILE))
        expected = {"num_customers": 3,
                    "max_wait": 10,
                    "total_time": 18}
        self.assertEqual(expected, actual,"2s时第一个人进来 他到12s才能结束买单, 第二个人5s进来这时它会被分配到express里他会在12s才能结束， 第三个人在10s进入，这时他只能进入第一条线，而在11s时线被close了，所以他必须在12s时进入express。那么他需要6s完成所以是18s")

    def test_15(self):
        CONFIG_FILE = '''{"regular_count": 1,
                          "express_count": 1,
                          "self_serve_count": 1,
                          "line_capacity": 1
                        }
                        '''
        EVENT_FILE = """17 Arrive Dino a 6
                        10 Arrive Tamara Bananas 7
                        8 Close 1
                        6 Close 0
                        5 Arrive Jugo Bread 3 Cheese 3"""
        gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
        actual = gss.run(StringIO(EVENT_FILE))
        expected = {"num_customers": 3,
                    "max_wait": 19,
                    "total_time": 36}
        self.assertEqual(expected, actual, "5s时第一个人进来他要到11s才能结束买单而6s和8s的时候regular和express都关了那么对于10s进来的self serve他需要到24s才能结束买单，而17s时有人进来了，但他只能去self serve，而这时self serve还有人所以他需要到24s才能买单，而他结束买单是在24 + 12 = 36s而他是在17s就已经来了，所以他等了19s")

    def test_16(self):
        CONFIG_FILE = '''{"regular_count": 1,
                     "express_count": 1,
                     "self_serve_count": 1,
                     "line_capacity": 1
                   }
                   '''
        EVENT_FILE = """23 Arrive Dino a 6
                   16 Close 0
                   10 Arrive Tamara a 1 b 2 c 3 d 4 e 5 f 6 g 7 h 8 i 9
                   9 Close 1
                   5 Arrive Jugo Bread 3 Cheese 3"""
        gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
        actual = gss.run(StringIO(EVENT_FILE))
        expected = {"num_customers": 3,
                    "max_wait": 90,
                    "total_time": 112}
        self.assertEqual(expected, actual,
                         "5s时第一个人进来到11s，而9s时第一条线已经关了，所以10s第二个人进来时必须到express， 而他又超过了限制，所以必须去self serve，而他需要完成的时间则是45 * 2 90s，他完成的时间是100s，而9s和16s第一条和第二条线都已经关闭了，所以第三人不得不去第三条，他不得不等第二个人结束买单才能开始买单，所以第三个人在100s才能开始买单，而他需要6 * 2s才能结束，所以112s才结束")

    # def test_17(self):
    #     CONFIG_FILE = '''{"regular_count": 1,
    #                  "express_count": 1,
    #                  "self_serve_count": 1,
    #                  "line_capacity": 2
    #                }
    #                '''
    #     EVENT_FILE = """23 Arrive Dino a 6
    #                23 Close 0
    #                10 Arrive Tamara a 1 b 2 c 3 d 4 e 5 f 6 g 7 h 8 i 9
    #                9 Close 1
    #                5 Arrive Jugo Bread 3 Cheese 3"""
    #     gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
    #     actual = gss.run(StringIO(EVENT_FILE))
    #     expected = {"num_customers": 3,
    #                 "max_wait": 90,
    #                 "total_time": 100}
    #     self.assertEqual(expected, actual,
    #                      "5s时第一个人进来到11s，而9s时第一条线已经关了，所以10s第二个人进来时必须到express， 而他超过了限制，所以必须去self serve，而他需要完成的时间则是45 * 2 90s，他完成的时间是100s，第三人在23s进入，这时他被分配到第一条线，所以他在29s就结束了买单")

if __name__ == '__main__':
    unittest.main(exit=False)

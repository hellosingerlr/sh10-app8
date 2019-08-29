import allure


@allure.step("测试计划1")
class Test001:
    def test001(self):
        print("test001")
        allure.attach("data")
        assert True

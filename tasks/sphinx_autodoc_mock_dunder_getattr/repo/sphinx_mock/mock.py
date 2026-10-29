class MockObject:
    def __getattr__(self, name: str):
        return MockObject()

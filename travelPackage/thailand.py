class ThailandPackage:
    def detail(self):
        print("[태국 패키지] 방콕, 파타야 투어")

if __name__ == "__main__": # 모듈 직접 실행
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 출력됨.")
    tripTo = ThailandPackage()
    tripTo.detail() # [태국 패키지] 방콕, 파타야 투어
else:
    print("Thailand 외부에서 모듈이 호출됨.") # 외부 파일에서 thailand 모듈 호출할 경우 출력
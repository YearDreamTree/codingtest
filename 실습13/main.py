from user읽기전용 import User

class Post:

    # 지시사항: 매개변수로 작성자 이름 author와 작성 내용 content를 받아 그 값을 적합한 속성에 저장하는 생성자를 정의하세요.
    # comments, blocks 역시 빈 리스트로 초기화 해야 합니다.
    
    
    
    # 지시사항: author와 comment를 매개변수로 받아 comments 속성 리스트에 추가하는 addComment 메서드를 정의하세요.
    
        
    
    # 지시사항: user를 입력받아 blocks에 없으면 추가하고, 이미 존재하면 제거하는 addBlock 메서드를 정의하세요.


        
    # 게시글과 댓글의 내용을 반환해주는 메서드입니다.
    def display(self, user):
        # 출력할 결과를 저장할 result 입니다.
        result = ""    
        # 차단 된 유저가 글을 볼 수 없도록 아래의 조건문을 작성합니다.
        if user not in self.blocks:
            result += "작성자: " + self.author.name
            result += "\n내  용: " + self.content
            result += "\n댓  글\n"
            for i in range(len(self.comments)):
                result += str(self.comments[i][1]) + "-" + str(self.comments[i][0].name) + "\n"
            
        else:
            result = "차단된 사용자입니다"
        
        return result

# 올바른 작동을 확인하기 위한 코드입니다.
author = User("Donald Trump")
user1 = User("John")
user2 = User("Jane")
user3 = User("Gone")
content = "Make America Great Again"
comment1 = "Hello"
comment2 = "Country roads, take me home"
comment3 = "R U serious?"
post = Post(author, content)
post.addComment(user1, comment1)
post.addComment(user2, comment2)
post.addComment(user3, comment3)
print(post.comments)

post.addBlock(user3)
print(post.display(user1))
print(post.display(user2))
print(post.display(user3))

import pandas as pd

# 기존 CSV 파일의 경로와 이름을 지정하세요.
input_file_path = 'D:\\Github\\han\\movie_for_you_team\\final_review_0.csv'

# CSV 파일을 읽습니다. 여기서는 'cp949' 인코딩을 사용합니다.
# 만약 'cp949'가 작동하지 않는다면 'ISO-8859-1'을 시도해보세요.
df = pd.read_csv(input_file_path, encoding='cp949')

# 새로운 파일 경로와 이름을 지정하세요.
output_file_path = 'D:\\Github\\han\\movie_for_you_team\\final_review_0.csv'

# CSV 파일을 'utf-8' 인코딩으로 다시 저장합니다.
df.to_csv(output_file_path, encoding='utf-8', index=False)

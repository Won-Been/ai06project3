from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('point_predict.pickle','rb')) #모델가져오기

#장르에 번호부여하기
dic = {'만화':2,
        '소설/시/희곡':3,
        '경제경영':4,
        '어린이':5,
        '건강/취미/레저':6,
        '에세이':7,
        '과학':8,
        '유아':9,
        '예술/대중문화':10,
        '인문학':11,
        '수험서/자격증':12,
        '좋은부모':13,
        '자기계발':14,
        '외국어':15,
        '사회과학':16,
        '청소년':17,
        '가정/요리/뷰티':18,
        '컴퓨터/모바일':19}

#처음 나오는 페이지
@app.route('/')
def home():
    return render_template('home.html')

#정보를 입력하고 submit을 클릭하면 predict페이지로 넘어가기
@app.route('/predict', methods=['GET','POST'])
def prediction():
    ranking = request.form['ranking']
    rating = request.form['rating']
    genre = request.form['genre']
    
    #우선 순위, 평점을 받고, 나머지는 0으로 채워두기
    li = [[int(ranking), float(rating)] + [0]*18]

    #클릭한 장르에 해당하는 자리에 1 넣기
    li[0][dic[genre]] = 1

    #해당 값들을 predict에 넣어 예상 sales point 값 받기
    prediction = model.predict(li)

    return str(prediction)
    

if __name__ == '__main__':
    app.run(debug=True)

SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME 
FROM ANIMAL_INS 
LEFT JOIN ANIMAL_OUTS 
ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID 
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME 
ORDER BY ANIMAL_INS.DATETIME;


SELECT ANIMAL_TYPE, ifnull(name, 'No name'), SEX_UPON_INTAKE 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;


SELECT A.NAME, A.DATETIME 
FROM ANIMAL_INS AS A 
LEFT JOIN ANIMAL_OUTS AS B 
ON A.ANIMAL_ID = B.ANIMAL_ID 
WHERE B.ANIMAL_ID IS NULL 
ORDER BY A.DATETIME ASC 
LIMIT 3;


SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME 
FROM ANIMAL_INS AS A 
LEFT JOIN ANIMAL_OUTS AS B 
ON A.ANIMAL_ID = B.ANIMAL_ID 
WHERE A.SEX_UPON_INTAKE LIKE 'Intact %'and (B.SEX_UPON_OUTCOME LIKE '%Spayed%' or B.SEX_UPON_OUTCOME LIKE '%Neutered%') 
ORDER BY A.ANIMAL_ID


SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS 
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty') 
WHERE NAME REGEXP '^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$' 
ORDER BY ANIMAL_ID


SELECT A.ANIMAL_ID, A.NAME 
FROM ANIMAL_INS AS A 
INNER JOIN ANIMAL_OUTS AS B 
ON A.ANIMAL_ID = B.ANIMAL_ID 
ORDER BY A.DATETIME - B.DATETIME 
LIMIT 2


SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜' 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID

DATE_FORMAT(column명, 날짜 포맷)
날짜 포맷
1. %Y = 4자리 연도
2. %y = 2자리 연도
3. %M = 월을 영어로 출력
4. %m = 월을 숫자로 출력
5. %D = 영어 포함(7th, 1st)
6. %d = 일을 숫자로 출력
7. %H = 24시간 시간 출력
8. %h = 12시간 시간 출력
'%y-%m-%d' = 21-02-23
'%y-%M-%D' = 21-February-23th


WITH RECURSIVE 
    cte AS 
    ( SELECT 0 AS HOUR 
        UNION ALL 
        SELECT HOUR + 1 
        FROM cte 
        WHERE HOUR < 23) 

SELECT cte.HOUR, COUNT(ANIMAL_OUTS.animal_id) 
FROM cte 
LEFT JOIN ANIMAL_OUTS 
on cte.HOUR = HOUR(ANIMAL_OUTS.DATETIME) 
GROUP BY cte.hour 
ORDER BY cte.hour




SELECT
 - 기본 조회 : SELECT * FROM TABLE_NAME : 테이블에서 모든 레코드 조회
 - 정렬 : SELECT COLUMN_NAME FROM TABLE_NAME ORDER BY COLUMN_NAME ASC : 순서대로 정렬 (생략 가능)
 - 역순 정렬 : SELECT COLUMN_NAME FROM TABLE_NAME ORDER BY COLUMN_NAME DESC : 역순으로 정렬
 - 조건 여러 개 정렬 : SELECT COLUMN_NAME FROM TABLE_NAME ORDER BY COLUMN_NAME1 ASC COLUMN_NAME2 DESC : COL1으로 정렬 후 같을 시 NAME2로 역순 정렬
 - 조건부 조회 : SELECT COLUMN_NAME FROM TABLE_NAME WHERE COLUMN_NAME =,!= '조건' ORDER BY ~~
 - 상위 n개 조회 : SELECT COLUMN_NAME FROM TABLE_NAME ORDER BY ~~ LIMIT n
 - 중복제거 : SELECT DISTINCT COLUMN_NAME FROM TABLE_NAME
 

WHERE 조건 ( 작은따옴표 사용하기)
 - 비교 : WHERE COLUMN_NAME < 20000 또는 COLUMN_NAME > 10000 AND COLUMN_NAME <= 20000
 - 범위 : WHERE COLUMN_NAME BETWEEN 10000 AND 20000 (위와 동일한 조건)
 - 집합 : WHERE COLUMN_NAME IN ('A', 'B')
 - 패턴 : WHERE NAME LIKE '~~~' 또는 '%축구%' ( 축구란 단어가 들어간 모두) 또는 '_구%' (두 번째 위치에 구가 해당)
 - NULL : WHERE COLUMN_NAME IS NULL 또는 IS NOT NULL
 - 복합 조건 : WHERE (COLUMN_NAME < 20000) AND (NAME LIKE '~~~')
 

집계 함수(MAX, MIN, SUM, AVG, COUNT)
 - 최댓값 : SELECT MAX(COLUMN_NAME) AS 원하는 이름 FROM TABLE_NAME
 - 최솟값 : SELECT MIN(COLUMN_NAME) AS 원하는 이름 FROM TABLE_NAME
 - 개수 : SELECT COUNT(COLUMN_NAME) AS 원하는 이름 FROM TABLE_NAME
 - 평균 : SELECT AVG(COLUMN_NAME) AS 원하는 이름 FROM TABLE_NAME
 - 총합 : SELECT SUM(COLUMN_NAME) AS 원하는 이름 FROM TABLE_NAME
 - NULL과 중복 제거한 개수 : SELECT COUNT(DISTINCT NAME) FROM TABLE WHERE NAME IS NOT NULL
 

GROUP BY - 속성 값이 같은 값끼리 그룹을 만들 수 있다.
예를 들어 GROUP BY custid일시 custid가 같은 값끼리 그룹을 묶는다.(1 끼리, 2 끼리, 3 끼리...)
ex) 고객별로 주문한 도서의 총수량과 총판매액을 구하시오.
SELECT custid, COUNT(*) AS 도서수량, SUM(saleprice) AS 총액
FROM Orders
GROUP BY custid;
 

HAVING - GROUP BY의 결과에 조건을 걸어주는 역할을 한다.
ex) 가격이 8천원 이상인 도서를 구매한 고객에 대하여 고객별 주문 도서의 총수량을 구하시오. 단, 두 권 이상 구매한 고객만 구하시오.
SELECT custid, COUNT(*) AS 도서수량
FROM Orders
WHERE saleprice >= 8000
GROUP BY custid
HAVING COUNT(*) >= 2
 

DATETIME에서 속성 추출
- HOUR(DATETIME COLUMN NAME) : TYPE이 DATETIME인 데이터에서 시간만 추출할 수 있다.
- MINUTE : 분 정보 추출
- SECOND : 초 정보 추출
ex)  09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

SELECT HOUR(DATETIME) HOUR, count(*) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 AND HOUR <= 19
ORDER BY HOUR(DATETIME)




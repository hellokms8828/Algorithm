-- 코드를 입력하세요
SELECT B.WRITER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B JOIN USED_GOODS_USER AS U
ON U.USER_ID = B.WRITER_ID
WHERE B.STATUS = 'DONE'
GROUP BY B.WRITER_ID
HAVING (SUM(B.PRICE) >= 700000)
ORDER BY TOTAL_SALES ASC
;
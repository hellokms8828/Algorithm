-- 코드를 입력하세요
SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') PUBLISHED_DATE FROM BOOK WHERE CATEGORY = '인문' and year(PUBLISHED_DATE) = 2021
ORDER BY PUBLISHED_DATE ASC;
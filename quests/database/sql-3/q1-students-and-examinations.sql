with s_s as (
    select student_id, student_name, subject_name 
    from students s
    cross join subjects
    order by student_id, subject_name
)
select s_s.*, count(e.student_id) as attended_exams
from s_s
left join examinations e 
    on s_s.student_id = e.student_id and s_s.subject_name = e.subject_name
group by s_s.student_id, s_s.student_name, s_s.subject_name

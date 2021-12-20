import axios from "axios";

export function vacancyListApi(
    experience = '',
    type_employment = '',
    work_schedule = '',
    education = '',
    remote_work = '',
    disability = '',
    sort = ''
) {
    const abs = 'test'
    const fetching = async () => {
        console.log('Я в функции')

        try{
            console.log('Я в функции')
            response = axios.get('http://127.0.0.1:8000/api/vacancies/', {
                params: {
                    experience: experience,
                    type_employment: type_employment,
                    work_schedule: work_schedule,
                    education: education,
                    remote_work: remote_work,
                    disability:  disability,
                    sort: sort
                }
            })
            console.log('Я закончил запрос')

        }catch (e) {
            console.log('Возникла ошибка')
            alert('Ошибка')
        } finally {
            console.log('Финал')
            //isPostsLoading.value = false;
            console.log('Финал')
        }
    } 
    return {fetching, abs}
}
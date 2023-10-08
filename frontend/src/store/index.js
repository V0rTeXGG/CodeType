import {createStore} from 'vuex'

export default createStore({
    state: {
        access: '',
        refresh: '',
        isLoader: true,
        languages: [
            {
                lang: 'JS',
                icon: require('@/assets/img/main/js-icon.svg'),
                task: [
                    'const filterEvenNumbers = (arr) => arr.filter((num) => num % 2 === 0)',
                    'const getRandomNumber = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min',
                    'const arraySum = arr => arr.reduce((total, num) => total + num, 0)',
                    'const truncateString = (str, maxLength) => str.length > maxLength ? str.slice(0, maxLength) + \'...\' : str',
                    'const countVowels = str => (str.match(/[aeiou]/gi) || []).length',
                    'const isPalindrome = str => str === str.split(\'\').reverse().join(\'\')',
                    'const randomHexColor = () => \'#\' + Math.floor(Math.random() * 16777215).toString(16)',
                    'const toCamelCase = str => str.replace(/[-_](.)/g, (_, c) => c.toUpperCase())',
                    'const mergeArrays = (arr1, arr2) => [...new Set([...arr1, ...arr2])]',
                    'const isNumber = val => typeof val === \'number\' && !isNaN(val)',
                ]
            },
            {
                lang: 'C++',
                icon: require('@/assets/img/main/C-icon.svg'),
                task: [
                    'squares_up_to_n = lambda N: [x ** 2 for x in range(1, N+1)]',
                    'is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))',
                    'factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)',
                    'sum_even = lambda N: sum(x for x in range(2, N+1, 2))',
                    'count_vowels = lambda s: sum(1 for c in s if c in \'aeiouAEIOU\')',
                    'print_even = lambda N: print(*range(2, N+1, 2))',
                    'is_prime = lambda n: n > 1 and all(n % i for i in range(2, n))',
                    'circle_area = lambda r: 3.14159 * r ** 2',
                ],

            },
            {
                lang: 'Python',
                icon: require('@/assets/img/main/python-icon.svg'),
                task: [
                    'int factorial(int n) { return (n == 0) ? 1 : n * factorial(n - 1); }',
                    'string reverse_string(string s) { reverse(s.begin(), s.end()); return s; }',
                    'string reverse_string(string s) { reverse(s.begin(), s.end()); return s; }',
                    'double celsius_to_fahrenheit(double c) { return c * 9/5 + 32; }',
                    'string to_upper(string s) { transform(s.begin(), s.end(), s.begin(), ::toupper); return s; }',
                    'void print_even(int N) { for (int i = 2; i <= N; i += 2) cout << i << \' \'; cout << endl; }',
                    'int count_letters(string s) { return count_if(s.begin(), s.end(), ::isalpha); }',
                    'int count_primes(int N) { return count_if(begin(N), end(N), is_prime); }',
                ]
            }
        ],
        selectLang: 'JS',
        isAuthorization: false,
        isTaskDone: false,
        username: '',
        userPassword: '',
        isModalVis: false,
        isActiveTask: false,

        isErrorMassage: false,
        isErrorMassageVoid: '',
    },
    getters: {},
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem("access")) {
                state.access = localStorage.getItem("access")
                state.refresh = localStorage.getItem("refresh")
            } else {
                state.access = ''
                state.refresh = ''
            }
        },
        setAccess(state, access) {
            state.access = access
        },
        setRefresh(state, refresh) {
            state.refresh = refresh
        },
        updateTaskStatus(state, newVal) {
            state.isTaskDone = newVal
        },
        updateActiveTask(state, newVal) {
            state.isActiveTask = newVal
        },
        updateModalStatus(state, newVal) {
            state.isModalVis = newVal
        },
        updateSelectLang(state, newVal) {
            state.selectLang = newVal
        },
        updateStatusAuthorization(state, newVal) {
            state.isAuthorization = newVal
            localStorage.setItem('isAuthorization', JSON.stringify(state.isAuthorization));
        },
        setUserName(state, newVal) {
            state.username = newVal
            localStorage.setItem('username', JSON.stringify(state.username));
        },
        setUserPassword(state, newVal) {
            state.userPassword = newVal
            localStorage.setItem('password', JSON.stringify(state.userPassword));
        },
        closeErrorMassage(state, newVal) {
            state.isErrorMassage = newVal
        },
        updateErrorMassageVoid(state, newVal) {
            state.isErrorMassage = newVal
            state.isErrorMassageVoid = 'Please fill in all fields'
        },
        updateErrorMassageCurrent(state, newVal) {
            state.isErrorMassage = newVal
            state.isErrorMassageVoid = 'Please fill in the following fields correctly'
        },
        updateErrorMassageNon(state, newVal) {
            state.isErrorMassage = newVal
            state.isErrorMassageVoid = 'There is no such data, please check that it is filled out correctly'
        },
    },
    actions: {
        async startTask({commit}, taskStatus) {
            try {
                commit('updateActiveTask', taskStatus)
            } catch (error) {
                console.log(error)
            }
        },
        async completeTask({commit}, taskStatus) {
            try {
                // commit('updateTaskStatus', taskStatus.status)
                commit('updateActiveTask', taskStatus.active)
            } catch (error) {
                console.log(error)
            }
        },
        async restartTask({commit}, taskStatus) {
            try {
                // commit('updateTaskStatus', taskStatus);
                commit('updateActiveTask', taskStatus);
            } catch (error) {
                console.log(error)
            }
        }
    },
    modules: {}
})

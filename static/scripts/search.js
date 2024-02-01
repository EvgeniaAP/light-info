const {Observable, of, fromEvent, debounceTime, switchMap} = rxjs

export class Searcher {
    searchEvent
    constructor(input) {
        this.input = input;
        this.searchEvent = fromEvent(this.input, 'input').pipe(debounceTime(500),switchMap(()=> {
            if(input.value?.length >= 3) {
                return this.search(input.value)
            } else {
                return of([])
            }
        }))

    }

    search(text) {
        if(this.request) {
            this.request.abort()
        }
        const xhr = new XMLHttpRequest()
        xhr.responseType = 'json'
        this.request = xhr;

        return Observable.create(function (observer) {
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === 4) {
                        if (xhr.status === 200) {
                            observer.next(xhr.response);
                            observer.complete();
                        } else {
                            observer.error(xhr.response);
                        }
                    }

                    return () => {
                        xhr.abort();
                    };
                }

                xhr.open('GET', `/search?text=${text}`)
                xhr.send()
            }
        )
        }


    }
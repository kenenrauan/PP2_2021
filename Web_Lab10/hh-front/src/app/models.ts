  export interface Company{
    id: number
    name : String
    description : String
    city : String
    address : String
  }
  export interface Vacancy{
    id: number
    name : String
    description : String
    salary : number
    company : number
  }
  export interface AuthToken {
    token: string;
  }

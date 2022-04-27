export interface Order {
  customer: number;
  product: Array<number>;
  date_created: Date;
  status: string;
  note: string;
}

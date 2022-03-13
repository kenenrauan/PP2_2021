export class Item {
  name: string;
  link: string;
  imageLink: string;
  description: string;
  rating: number;
  categoryId: number;
  likes: number;

  constructor(data: any) {
    this.name = data?.name || '';
    this.link = data?.link || '';
    this.imageLink = data?.imageLink || '';
    this.description = data?.description || '';
    this.rating = data?.rating || 0;
    this.categoryId = data?.categoryId || 0;
    this.likes = data?.likes || 0;
  }
}

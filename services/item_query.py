from repositories.item_repository import ItemRepository


class ItemQuery:

    @staticmethod
    def all():
        return ItemRepository.get_all()

    @staticmethod
    def get(item_id):
        return ItemRepository.get_by_id(item_id)

    @staticmethod
    def search(name):
        return ItemRepository.search(name)
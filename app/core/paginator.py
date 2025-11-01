from typing import List, TypeVar, Dict, Any

T = TypeVar("T")


def pagenation(
    data: List[T],
    page_number=1,
    page_size=20,
    start_page_as_1=True,
) -> Dict[str, Any]:
    """Return payload that contains metainformations about
    pagination and listing data.
    page_number starts with 0 (array like),
    if start_page_as_1 defined as True, start with 1.

    Args:
        page_number: Current page number
        page_size: Number of items per page
        total_count: Total number of items
        data: List of items of type T to be paginated
        start_page_as_1: If True, page_number starts at 1, otherwise at 0

    Returns:
        Dictionary containing pagination metadata and sliced data
    """
    total_count = len(data)
    if start_page_as_1:
        if page_number <= 0:
            raise Exception(
                "Page number must starts > 0.\nCause: start_page_as_1=True and page_number defined as <= 0"
            )
        else:
            page_number -= 1
    remaining = total_count % page_size
    total_pages = (
        total_count // page_size + 1 if remaining else total_count // page_size
    )
    begin = page_number * page_size
    end = begin
    if page_number == total_pages and remaining:
        end += remaining
    else:
        end += page_size

    listings = data[begin:end] if data is not None else []

    return {
        "begin": begin,
        "end": end,
        "totalPages": total_pages,
        "remaining": remaining,
        "pageNumber": page_number,
        "pageSize": page_size,
        "totalCount": total_count,
        "listings": listings,
    }

"""Pillow 兼容性补丁。"""

from __future__ import annotations


def ensure_antialias_alias() -> bool:
    """为 Pillow 新版本补齐 ``Image.ANTIALIAS`` 别名。

    Pillow 在新版本中移除了 ``Image.ANTIALIAS``，旧代码或三方依赖
    仍可能访问该属性。此函数在运行时补齐别名，避免抛出
    ``AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'``。

    Returns:
        bool: 是否执行了补丁（True 表示本次新增了别名）。
    """
    try:
        from PIL import Image
    except Exception:
        return False

    if hasattr(Image, "ANTIALIAS"):
        return False

    resampling = getattr(Image, "Resampling", None)
    lanczos = getattr(resampling, "LANCZOS", None) if resampling else None
    if lanczos is None:
        return False

    Image.ANTIALIAS = lanczos
    return True

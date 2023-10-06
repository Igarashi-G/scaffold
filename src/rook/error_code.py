# code: 0 0 F F F F
#       \-/ \-/ \-/
#         \--------- 类别
#             \--------- 标识码
#                 \--------- 错误码


# @formatter:off
class StatusCode:
    STATUS_SUCCESS                                  = 0  # noqa  操作成功
    STATUS_FAILED                                   = 1  # noqa  操作失败

    # rpc error
    STATUS_RPC_UNKNOWN                              = 100001  # noqa  RPC调用出现未知错误
    STATUS_RPC_CANCELLED                            = 100002  # noqa  RPC调用被取消
    STATUS_RPC_INVALID_PARAMETER                    = 100003  # noqa  RPC调用出现非法的请求参数
    STATUS_RPC_DEADLINE_EXCEEDED                    = 100004  # noqa  RPC调用超时
    STATUS_RPC_NOT_FOUND                            = 100005  # noqa  RPC调用不存在
    STATUS_RPC_ABORTED                              = 100007  # noqa  RPC异常终止
    STATUS_RPC_OUT_OF_RANGE                         = 100008  # noqa  RPC栈溢出
    STATUS_RPC_UNIMPLEMENTED                        = 100009  # noqa  RPC调用的服务未实现
    STATUS_RPC_UNAUTHENTICATED                      = 100010  # noqa  RPC认证失败
    STATUS_RPC_PERMISSION_DENIED                    = 100011  # noqa  RPC调用的权限不足
    STATUS_RPC_UNAVAILABLE                          = 100012  # noqa  RPC服务不可用(网络不通)
    STATUS_RPC_PROTOCOL_ERROR                       = 100013  # noqa  RPC协议错误
    STATUS_RPC_INTERNAL_ERROR                       = 100014  # noqa  RPC内部错误

    STATUS_INVALID_PARAMETER                        = 110001  # noqa  参数错误
    STATUS_NOT_SUPPORT_ERROR                        = 110002  # noqa  不支持此业务
    STATUS_SERVICE_UNAVAILABLE                      = 110003  # noqa  服务不可用
    STATUS_UNSUPPORT_FSTYPE                         = 110004  # noqa  不支持的文件系统格式

    STATUS_NODE_NOT_EXISTS                          = 120000  # noqa  节点不存在
    STATUS_NODE_ALREADY_EXISTS                      = 120001  # noqa  节点已存在
    STATUS_NODE_IS_OFFLINE                          = 120002  # noqa  节点不在线
    STATUS_IPADDR_NOT_EXISTS                        = 120003  # noqa  IP地址不存在
    STATUS_CONFIG_FILE_ERROR                        = 120004  # noqa  配置文件拷贝失败
    STATUS_NODE_IN_OTHER_CLUSTER                    = 120005  # noqa  节点已经加入过其他集群
    STATUS_NODE_ADD_FAILED                          = 120006  # noqa  节点添加失败
    STATUS_NODE_SERVICE_EXISTS                      = 120007  # noqa  节点仍有服务存在
    STATUS_NODE_PROHIBIT_DELETION                   = 120008  # noqa  节点禁止删除
    STATUS_NODE_FILE_TOO_BIG                        = 120009  # noqa  文件超过限定传输大小
    STATUS_NODE_MACHINE_ID_INVAILD                  = 120010  # noqa  无效的machine id
    STATUS_FILE_PATTERN_ERROR                       = 120011  # noqa  文件格式错误
    STATUS_UFS_STOP_FAILED                          = 120012  # noqa  文件存储未停止成功
    STATUS_UUS_STOP_FAILED                          = 120013  # noqa  块存储未停止成功
    STATUS_RRD_TIME_NOT_SATISFY                     = 120014  # noqa  查询时间超出支持范围
    STATUS_UUS_NODE_CAN_NOT_SHUTDOWN                = 120015  # noqa  块存储超出容错保护
    STATUS_UUS_NODE_CAN_NOT_REBOOT                  = 120016  # noqa  块存储超出容错保护
    STATUS_PD_SERVER_NOT_EXISTS                     = 120017  # noqa  Pd 服务不存在
    STATUS_PD_SERVER_EXISTS                         = 120018  # noqa  Pd 服务已存在
    STATUS_TIKV_SERVER_EXISTS                       = 120019  # noqa  Tikv服务已存在
    STATUS_PD_INIT_FAILED                           = 120020  # noqa  Pd服务初始化失败
    STATUS_TIKV_INIT_FAILED                         = 120021  # noqa  Tikv服务初始化失败
    STATUS_RAFT_CONFIG_FAILED                       = 120022  # noqa  节点选举配置失败


    STATUS_UFSMOUNT_UNAVAILABLE                     = 130001  # noqa  内部客户端未就绪
    STATUS_CLUSTER_UNAVAILABLE                      = 130002  # noqa  存储集群未就绪
    STATUS_PLATFORM_UNAVAILABLE                     = 130003  # noqa  存储平台未初始化
    STATUS_PLATFORM_UNABLE                          = 130004  # noqa  初始化检查未通过
    STATUS_PLATFORM_FAILED                          = 130005  # noqa  初始化平台失败
    STATUS_PLATFORM_DATA_FAILED                     = 130006  # noqa  初始化平台数据失败
    STATUS_PLATFORM_HEALTH_ERROR                    = 130007  # noqa  平台数据源异常
    STATUS_PLATFORM_ETCD_CONNECTION_FAILED          = 130008  # noqa  平台数据库连接异常

    STATUS_MSS_ALREADY_EXISTS                       = 140001  # noqa  mss服务已存在
    STATUS_MSS_NOT_EXISTS                           = 140002  # noqa  mss服务不存在
    STATUS_CSS_ALREADY_EXISTS                       = 140003  # noqa  css服务已存在
    STATUS_CSS_NOT_EXISTS                           = 140004  # noqa  css服务不存在
    STATUS_MSS_DEL_FAILED                           = 140005  # noqa  mss服务删除失败
    STATUS_CSS_DEL_FAILED                           = 140006  # noqa  css服务删除失败
    STATUS_MSS_IS_RUNNING                           = 140007  # noqa  mss服务正在运行
    STATUS_CSS_IS_RUNNING                           = 140008  # noqa  css服务正在运行
    STATUS_UUS_ALREADY_EXISTS                       = 140009  # noqa  uus服务已存在
    STATUS_UUS_GET_FAILED                           = 140010  # noqa  uus服务获取失败
    STATUS_UUS_NODE_ID_NOT_EXISTS                   = 140010  # noqa  uus服务ID不存在
    STATUS_EC_STOP_FAILED                           = 140011  # noqa  ec服务停止失败

    STATUS_NOT_DIR_ERROR                            = 150001  # noqa  操作对象不是目录
    STATUS_IS_DIR_ERROR                             = 150002  # noqa  操作对象是目录
    STATUS_FILE_NOT_EXISTS                          = 150003  # noqa  文件不存在
    STATUS_FILE_EXISTS                              = 150004  # noqa  文件已存在
    STATUS_FILE_NOT_IN_SAMEDIR                      = 150005  # noqa  文件不在同一个目录
    STATUS_DIR_NOT_EXISTS                           = 150006  # noqa  目录不存在
    STATUS_DIR_NOT_EMPTY                            = 150007  # noqa  目录非空
    STATUS_SC_IN_USE                                = 150008  # noqa  存储策略正被使用，无法删除
    STATUS_SC_EXISTS                                = 150009  # noqa  存储策略已存在，无法再次创建
    STATUS_NUMBER_OF_TRASH_FILE_TOO_LARGE           = 150010  # noqa  回收站文件数量过大，请去后台手动执行相关操作
    STATUS_TRASH_FILE_IS_BEING_DELETED              = 150011  # noqa  正在清空回收站，请稍后再试。
    STATUS_FILE_NUMBER_IS_TOO_BIG                   = 150012  # noqa  文件数量过大，请在后台手动配置。
    STATUS_SCLASS_NOT_EXISTS                        = 150013  # noqa  存储策略不存在

    STATUS_USER_NOT_EXISTS                          = 160001  # noqa  用户不存在
    STATUS_USER_ALREADY_EXISTS                      = 160002  # noqa  用户已存在
    STATUS_GROUP_NOT_EXISTS                         = 160003  # noqa  组不存在
    STATUS_GROUP_ALREADY_EXISTS                     = 160004  # noqa  组已存在
    STATUS_INVALID_ACTION                           = 160005  # noqa  无效的操作
    STATUS_CHNANGE_PASSWORD_FAILED                  = 160006  # noqa  修改密码失败
    STATUS_INCORRECT_USERNAME_OR_PASSWORD           = 160007  # noqa  无效的用户名或密码
    STATUS_CREATE_PARTIAL_FAILURE                   = 160008  # noqa  部分节点创建失败
    STATUS_UPDATE_PARTIAL_FAILURE                   = 160009  # noqa  部分节点更新失败
    STATUS_DELETE_PARTIAL_FAILURE                   = 160010  # noqa  部分节点删除失败
    STATUS_UNAUTHORIZED_ACTION                      = 160011  # noqa  无权限操作
    STATUS_ROLE_NOT_EXISTS                          = 160012  # noqa  角色不存在
    STATUS_ROLE_ALREADY_EXISTS                      = 160013  # noqa  角色已存在
    STATUS_ROLE_OCCUPIED                            = 160014  # noqa  角色被用户占用
    STATUS_USER_NOT_SYNCED                          = 160015  # noqa  本地用户未同步，请同步
    STATUS_GROUP_NOT_SYNCED                         = 160016  # noqa  本地用户组未同步，请同步
    STATUS_ANY_ACL_SYNCED_FAILED                    = 160017  # noqa  部分节点用户/组同步失败
    STATUS_ALL_ACL_SYNCED_FAILED                    = 160018  # noqa  本地用户/组同步失败
    STATUS_GID_ALREADY_EXISTS                       = 160019  # noqa  用户组GID已存在，请更换
    STATUS_UID_ALREADY_EXISTS                       = 160020  # noqa  用户UID已存在，请更换
    STATUS_INCORRECT_ORIGINAL_PASSWORD              = 160021  # noqa  原密码错误

    STATUS_RESOURCES_OCCUPIED                       = 170001  # noqa  资源被占用

    STATUS_SET_FAILED                               = 180001  # noqa  设置失败
    STATUS_EMAIL_CONNECT_FAILED                     = 180002  # noqa  邮件服务器连接失败
    STATUS_EMAIL_AUTH_FAILED                        = 180003  # noqa  邮件用户认证失败
    STATUS_EMAIL_SEND_FAILED                        = 180004  # noqa  邮件发送失败
    STATUS_EMAIL_REFUSED                            = 180005  # noqa  邮件被服务端拒收
    STATUS_EMAIL_NOT_CONFIGURED                     = 180006  # noqa  未保存邮件配置
    STATUS_EMAIL_LEVEL_UNCHECKED                    = 180007  # noqa  此告警等级未在邮件中配置

    STATUS_SNMP_NOT_CONFIGURED                      = 190001  # noqa  未保存SNMP配置

    STATUS_DOMAIN_VIP_OCCUPIED                      = 210001  # noqa  保护域VIP已被占用
    STATUS_DOMAIN_NODE_IP_NOT_EXISTS                = 210002  # noqa  保护域节点IP不存在
    STATUS_DOMAIN_INIT_ERROR                        = 210003  # noqa  保护域初始化失败
    STATUS_DOMAIN_VIP_CONFIG_ERROR                  = 210004  # noqa  保护域VIP配置失败
    STATUS_DOMAIN_ADD_UUS_FAILED                    = 210004  # noqa  保护域添加后续服务失败
    STATUS_DOMAIN_DELETE_UUS_FAILED                 = 210005  # noqa  保护域仍有块服务存在
    STATUS_DOMAIN_FORCE_REMOVE_LEADER_UUS_ERROR     = 210009  # noqa  保护域强制删除Leader块服务出错
    STATUS_DOMAIN_FORCE_REMOVE_UUS_ERROR            = 210008  # noqa  保护域强制删除块服务出错
    STATUS_DOMAIN_FORCE_REMOVE_UUS_FAILED           = 210007  # noqa  保护域强制删除块服务失败
    STATUS_DOMAIN_SYNC_LIMIT_FAILED                 = 210006  # noqa  保护域重构速度应在150~30之间或者等于零
    STATUS_DOMAIN_HASE_UNREMOVE_UUS                 = 210010  # noqa  保护域存在未删除的块服务
    STATUS_DOMAIN_VIP_REMOVE_FAILED                 = 210011  # noqa  保护域VIP删除失败
    STATUS_DOMAIN_NOT_FOUND                         = 210012  # noqa  保护域不存在
    STATUS_DOMAIN_HASE_OFFLINE_NODE                 = 210013  # noqa  保护域中有离线节点
    STATUS_DOMAIN_ALREADY_EXIST                     = 210014  # noqa  保护域已存在

    STATUS_UUS_UNINITIALIZED                        = 220001  # noqa  保护域未初始化存储服务
    STATUS_UUS_NEED_LICENSE                         = 220002  # noqa  块存储服务需要上传license
    STATUS_UUS_REMOVE_FAILED                        = 220003  # noqa  块存储服务删除失败
    STATUS_UUS_DATABASE_FAILED                      = 220004  # noqa  块存储服务数据获取失败
    STATUS_UUS_DATABASE_STORAGEFAILED               = 220005  # noqa  块存储服务数据存储失败

    STATUS_POOL_CREATE_FAILED                       = 230001  # noqa  存储池创建失败
    STATUS_POOL_UPDATE_FAILED                       = 230002  # noqa  存储池编辑失败
    STATUS_POOL_REMOVE_FAILED                       = 230003  # noqa  存储池移除失败
    STATUS_POOL_AUTO_BALANCE_FAILED                 = 230004  # noqa  存储池自动均衡失败
    STATUS_POOL_AUTO_ADD_DISK_FAILED                = 230005  # noqa  存储池自动加盘失败
    STATUS_POOL_ALLOCATED_FAILED                    = 230006  # noqa  存储池预分配虚拟磁盘失败
    STATUS_POOL_NOT_FOUND                           = 230007  # noqa  存储池不存在
    STATUS_POOL_JOURNAL_CANNOT_REMOVE               = 270008  # noqa  日志池不能删除
    STATUS_POOL_BALANCE_LIMIT_FAILED                = 270009  # noqa  配置均衡限速失败
    STATUS_POOL_HASE_NO_DISK                        = 270010  # noqa  存储池没有磁盘
    STATUS_DOMAIN_NOT_HASE_POOL                     = 270011  # noqa  保护域没有存储池

    STATUS_DISK_ADD_TO_POOL_FAILED                  = 240001  # noqa  磁盘未能添加到存储池中
    STATUS_DISK_REMOVE_FROM_POOL_FAILED             = 240002  # noqa  磁盘删除失败
    STATUS_DISK_ZERO_SUPER_BLOCK_FAILED             = 240003  # noqa  磁盘清除超块失败
    STATUS_DISK_UPDATE_FAILED                       = 240004  # noqa  磁盘更新失败
    STATUS_DISK_MIGRATE_FAILED                      = 240005  # noqa  磁盘迁移失败
    STATUS_DISK_LIST_IN_POOL_FAILED                 = 240006  # noqa  获取存储池磁盘失败

    STATUS_VDISK_CREATE_FAILED                      = 250001  # noqa  虚拟磁盘创建失败
    STATUS_VDISK_ROLLBACK_FAILED                    = 250002  # noqa  虚拟磁盘创建回滚失败
    STATUS_VDISK_DELETE_FAILED                      = 250003  # noqa  虚拟磁盘删除失败, 请检查是否已被使用
    STATUS_VDISK_NOT_FOUND                          = 250004  # noqa  虚拟磁盘不存在
    STATUS_VDISK_START_FAILED                       = 250005  # noqa  虚拟磁盘启动失败
    STATUS_VDISK_STOP_FAILED                        = 250006  # noqa  虚拟磁盘停止失败
    STATUS_VDISK_THICK_NAMESPACE_FAILED             = 250007  # noqa  厚置备卷失败
    STATUS_VDISK_ENABLE_JOURNAL_FAILED              = 250008  # noqa  启用日志卷失败
    STATUS_VDISK_DISABLE_JOURNAL_FAILED             = 250009  # noqa  停用日志卷失败
    STATUS_VDISK_RAID1_NO_SUPPORT_JOURNAL_FAILED    = 250013  # noqa  raid1不支持日志卷
    STATUS_VDISK_NAMESPACE_REMOVE_FAILED            = 250014  # noqa  卷删除失败
    STATUS_VDISK_IS_STOP                            = 250015  # noqa  虚拟磁盘未启动
    STATUS_VDISK_ALREADY_EXISTS                     = 250016  # noqa  虚拟磁盘已存在
    STATUS_VDISK_CAPACITY_UNIT_ERROR                = 250017  # noqa  虚拟磁盘单位错误
    STATUS_VDISK_CAPACITY_LESS_THAN_ZERO            = 250018  # noqa  虚拟磁盘容量小于等于零

    STATUS_NAMESPACE_ALREADY_EXISTS                 = 250020  # noqa  卷已存在
    STATUS_NAMESPACE_CREATE_FAILED                  = 250021  # noqa  卷创建失败
    STATUS_NAMESPACE_EXTEND_FAILED                  = 250022  # noqa  卷扩容失败

    STATUS_SNAPSHOT_CREATE_FAILED                   = 250030  # noqa  快照创建失败
    STATUS_SNAPSHOT_DELETE_FAILED                   = 250031  # noqa  快照删除失败
    STATUS_SNAPSHOT_UPDATE_FAILED                   = 250032  # noqa  快照更新失败
    STATUS_SNAPSHOT_DOMAIN_MAX_LIMIT_EXCEEDED       = 250033  # noqa  集群快照上限1024个
    STATUS_SNAPSHOT_NAMESPACE_MAX_LIMIT_EXCEEDED    = 250034  # noqa  单卷快照上限64个
    STATUS_SNAPSHOT_ALREADY_EXISTS                  = 250035  # noqa  快照已经存在

    STATUS_VOLUME_CACHE_SET                         = 250010  # noqa  数据卷设置缓存加速失败
    STATUS_VOLUME_CACHE_DELETE                      = 250011  # noqa  数据卷删除缓存加速失败
    STATUS_VOLUME_CACHE_GET                         = 250012  # noqa  数据卷获取缓存信息失败

    STATUS_ISCSI_CREATE_FAILED                      = 260001  # noqa  iSCSI导出创建失败
    STATUS_ISCSI_ADD_INITIATOR_FAILED               = 260002  # noqa  iSCSI导出添加发起端失败
    STATUS_ISCSI_DELETE_INITIATOR_FAILED            = 260003  # noqa  iSCSI删除发起端失败
    STATUS_ISCSI_UPDATE_INITIATOR_FAILED            = 260003  # noqa  iSCSI导出修改发起端失败
    STATUS_ISCSI_DELETE_FAILED                      = 260004  # noqa  iSCSI导出删除失败
    STATUS_ISCSI_NIC_NOT_FOUND                      = 260005  # noqa  iSCSI网卡不存在
    STATUS_ISCSI_NIC_DELETE_FAILED                  = 260006  # noqa  iSCSI网卡删除失败
    STATUS_ISCSI_UPDATE_CHAP_FAILED                 = 260007  # noqa  iSCSI配置chap失败
    STATUS_ISCSI_DELETE_CHAP_FAILED                 = 260008  # noqa  iSCSI删除chap失败

    STATUS_ISCSI_INITIATOR_ALREADY_EXISTS           = 260020  # noqa  iSCSI发起端已存在
    STATUS_ISCSI_LIST_INITIATOR_FAILED              = 260021  # noqa  iSCSI获取发起端失败
    STATUS_ISCSI_DELETE_VIP_FAILED                  = 260022  # noqa  iSCSI删除VIP失败
    STATUS_ISCSI_SET_VIP_FAILED                     = 260023  # noqa  iSCSI配置VIP失败
    STATUS_ISCSI_GET_VIP_FAILED                     = 260024  # noqa  iSCSI获取VIP失败
    STATUS_ISCSI_SET_NIC_FAILED                     = 260025  # noqa  iSCSI配置NIC失败

    STATUS_UUS_SERVER_ATTACH_FAILED                 = 270001  # noqa  UUS server 退出维护失败
    STATUS_UUS_SERVER_DETACH_FAILED                 = 270002  # noqa  UUS server 进入维护失败
    STATUS_UUS_SERVER_ALREADY_ADD                   = 270003  # noqa  UUS server 已经添加存在

    STATUS_NAS_ALREADY_EXISTS                       = 300001  # noqa  nas服务已存在
    STATUS_NAS_NOT_EXISTS                           = 300002  # noqa  nas服务不存在
    STATUS_NAS_IS_RUNNING                           = 300003  # noqa  nas服务正在运行
    STATUS_NAS_UNINITIALIZED                        = 300004  # noqa  未初始化文件网关服务
    STATUS_CES_ALREADY_EXISTS                       = 300005  # noqa  高可用服务已存在
    STATUS_CES_NOT_EXISTS                           = 300006  # noqa  高可用服务不存在
    STATUS_CES_NOT_IN_IP_POOL                       = 300007  # noqa  高可用期望IP不在IP池中
    STATUS_CES_IP_IS_USED                           = 300008  # noqa  高可用期望IP已被使用
    STATUS_CES_POOL_CAN_BE_PINGED                   = 300009  # noqa  高可用IP池内IP可被ping通
    STATUS_CES_POOL_LIMIT_REACHED                   = 300010  # noqa  高可用IP池的IP个数已达到上限

    STATUS_NFS_SHARE_ALREADY_EXISTS                 = 310001  # noqa  NFS共享已存在
    STATUS_NFS_SHARE_NOT_EXISTS                     = 310002  # noqa  NFS共享不存在
    STATUS_NFS_SHARE_CLIENT_ALREADY_EXISTS          = 310003  # noqa  共享客户端已存在
    STATUS_NFS_SHARE_MOUNT_FAILED                   = 310004  # noqa  NFS共享挂载失败
    STATUS_NFS_SHARE_UMOUNT_FAILED                  = 310005  # noqa  NFS共享挂载点卸载失败
    STATUS_NFS_SHARE_SYNCED_FAILED                  = 310006  # noqa  部分节点NFS导出同步失败

    STATUS_CIFS_NAME_ALREADY_EXISTS                 = 320001  # noqa  CIFS共享名称已存在
    STATUS_CIFS_PATH_ALREADY_EXISTS                 = 320002  # noqa  CIFS共享路径已存在
    STATUS_CIFS_SHARE_NOT_EXISTS                    = 320003  # noqa  CIFS共享不存在
    STATUS_CIFS_ACL_USER_NOT_EXISTS                 = 320004  # noqa  访问用户不存在
    STATUS_CIFS_ACL_USER_ALREADY_EXISTS             = 320005  # noqa  访问用户已存在
    STATUS_CIFS_ACL_GROUP_NOT_EXISTS                = 320006  # noqa  访问组不存在
    STATUS_CIFS_ACL_GROUP_ALREADY_EXISTS            = 320007  # noqa  访问组已存在
    STATUS_CIFS_USER_GET_FAILED                     = 320008  # noqa  获取CIFS用户数据失败
    STATUS_CIFS_USER_ADD_FAILED                     = 320009  # noqa  添加CIFS用户数据失败
    STATUS_CIFS_USER_UPDATE_FAILED                  = 320010  # noqa  修改CIFS用户数据失败
    STATUS_CIFS_USER_DETELE_FAILED                  = 320011  # noqa  删除CIFS用户数据失败
    STATUS_CIFS_SHARE_SYNCED_FAILED                 = 320012  # noqa  部分节点CIFS共享同步失败

    STATUS_NAMESERVICE_DOMAIN_CONNECT_FAILED        = 330001  # noqa  目标域连接失败
    STATUS_NAMESERVICE_AD_TIME_UNSYNC               = 330002  # noqa  主机与AD域时差过大
    STATUS_NAMESERVICE_CONFIG_WRITE_FAILED          = 330003  # noqa  域相关配置文件写入失败
    STATUS_NAMESERVICE_AD_HAS_JOINED                = 330004  # noqa  主机已经加入AD域
    STATUS_NAMESERVICE_AD_JOIN_FAILED               = 330005  # noqa  节点加入AD域失败
    STATUS_NAMESERVICE_DOMAIN_NOT_CONFIG            = 330006  # noqa  当前集群未加入过域，请先加域
    STATUS_NAMESERVICE_DOMAIN_NOT_FOUND             = 330007  # noqa  节点已不在域中
    STATUS_NAMESERVICE_LDAP_CONNECT_FAILED          = 330008  # noqa  LDAP连接失败
    STATUS_NAMESERVICE_LDAP_JOIN_FAILED             = 330009  # noqa  节点加入LDAP失败
    STATUS_NAMESERVICE_DOMAIN_SAME_HOSTNAME         = 330010  # noqa  存在相同的hostname

    STATUS_ALERT_CONFIG_ALREADY_EXISTS              = 400001  # noqa  告警配置已存在
    STATUS_ALERT_CONFIG_NOT_EXISTS                  = 400002  # noqa  告警配置不存在
    STATUS_ALERT_EVENT_NOT_EXISTS                   = 400003  # noqa  告警事件不存在


def error_code_to_message(code):
    code_tab = {
        StatusCode.STATUS_SUCCESS: "操作成功",
        StatusCode.STATUS_FAILED: "操作失败",

        StatusCode.STATUS_RPC_UNKNOWN: "操作失败，请查看操作日志获取错误原因",
        StatusCode.STATUS_RPC_CANCELLED: "RPC调用被取消",
        StatusCode.STATUS_RPC_INVALID_PARAMETER: "RPC调用出现非法的请求参数",
        StatusCode.STATUS_RPC_DEADLINE_EXCEEDED: " 系统资源不足，请稍后重试",
        StatusCode.STATUS_RPC_NOT_FOUND: "RPC调用不存在",
        StatusCode.STATUS_RPC_ABORTED: "RPC异常终止",
        StatusCode.STATUS_RPC_OUT_OF_RANGE: "RPC栈溢出",
        StatusCode.STATUS_RPC_UNIMPLEMENTED: "RPC调用的服务未实现",
        StatusCode.STATUS_RPC_UNAUTHENTICATED: "RPC认证失败",
        StatusCode.STATUS_RPC_PERMISSION_DENIED: "RPC调用的权限不足",
        StatusCode.STATUS_RPC_UNAVAILABLE: "RPC服务不可用",
        StatusCode.STATUS_RPC_PROTOCOL_ERROR: "RPC协议错误",

        StatusCode.STATUS_INVALID_PARAMETER: "参数错误",
        StatusCode.STATUS_NOT_SUPPORT_ERROR: "不支持此业务",
        StatusCode.STATUS_SERVICE_UNAVAILABLE: "服务不可用",
        StatusCode.STATUS_UNSUPPORT_FSTYPE: "不支持的文件系统格式",

        StatusCode.STATUS_NODE_NOT_EXISTS: "节点不存在",
        StatusCode.STATUS_NODE_ALREADY_EXISTS: "节点已存在",
        StatusCode.STATUS_IPADDR_NOT_EXISTS: "IP地址不存在",
        StatusCode.STATUS_NODE_IS_OFFLINE: "节点不在线",
        StatusCode.STATUS_CONFIG_FILE_ERROR: "配置文件拷贝失败",
        StatusCode.STATUS_NODE_IN_OTHER_CLUSTER: "节点已经加入过其他集群",
        StatusCode.STATUS_NODE_ADD_FAILED: "节点添加失败",
        StatusCode.STATUS_NODE_SERVICE_EXISTS: "节点仍有服务存在",
        StatusCode.STATUS_NODE_PROHIBIT_DELETION: "节点禁止删除",
        StatusCode.STATUS_NODE_FILE_TOO_BIG: "文件超过限定传输大小",
        StatusCode.STATUS_NODE_MACHINE_ID_INVAILD: "无效的machine id",
        StatusCode.STATUS_FILE_PATTERN_ERROR: "文件格式错误",
        StatusCode.STATUS_UFS_STOP_FAILED: "文件存储未停止成功",
        StatusCode.STATUS_UUS_STOP_FAILED: "块存储未停止成功",
        StatusCode.STATUS_UUS_NODE_CAN_NOT_SHUTDOWN: "超出容错保护，关机被拒绝，可选择关闭集群",
        StatusCode.STATUS_UUS_NODE_CAN_NOT_REBOOT: "超出容错保护，重启被拒绝，可选择关闭集群",
        StatusCode.STATUS_RRD_TIME_NOT_SATISFY: "查询时间超出支持范围",
        StatusCode.STATUS_PD_SERVER_NOT_EXISTS: "Pd 服务不存在",
        StatusCode.STATUS_PD_SERVER_EXISTS: "Pd 服务已存在",
        StatusCode.STATUS_TIKV_SERVER_EXISTS: "Tikv服务已存在",
        StatusCode.STATUS_PD_INIT_FAILED: "Pd服务初始化失败",
        StatusCode.STATUS_TIKV_INIT_FAILED: "Tikv服务初始化失败",
        StatusCode.STATUS_RAFT_CONFIG_FAILED: "节点配置失败",

        StatusCode.STATUS_UFSMOUNT_UNAVAILABLE: "内部客户端未就绪",
        StatusCode.STATUS_CLUSTER_UNAVAILABLE: "存储集群未就绪",
        StatusCode.STATUS_PLATFORM_UNAVAILABLE: "存储平台未初始化",
        StatusCode.STATUS_PLATFORM_UNABLE: "初始化检查未通过",
        StatusCode.STATUS_PLATFORM_FAILED: "初始化平台失败",
        StatusCode.STATUS_PLATFORM_DATA_FAILED: "初始化平台数据失败",
        StatusCode.STATUS_PLATFORM_HEALTH_ERROR: "平台数据源异常",
        StatusCode.STATUS_PLATFORM_ETCD_CONNECTION_FAILED: "平台数据库连接异常",

        StatusCode.STATUS_MSS_ALREADY_EXISTS: "mss服务已存在",
        StatusCode.STATUS_MSS_NOT_EXISTS: "mss服务不存在",
        StatusCode.STATUS_MSS_DEL_FAILED: "mss服务删除失败",
        StatusCode.STATUS_MSS_IS_RUNNING: "mss服务正在运行",


        StatusCode.STATUS_CSS_ALREADY_EXISTS: "css服务已存在",
        StatusCode.STATUS_CSS_NOT_EXISTS: "css服务不存在",
        StatusCode.STATUS_CSS_DEL_FAILED: "css服务删除失败",
        StatusCode.STATUS_CSS_IS_RUNNING: "css服务正在运行",
        StatusCode.STATUS_UUS_ALREADY_EXISTS: "uus服务已存在",
        StatusCode.STATUS_UUS_GET_FAILED: "uus服务获取失败",
        StatusCode.STATUS_UUS_NODE_ID_NOT_EXISTS: "uus服务ID不存在",
        StatusCode.STATUS_EC_STOP_FAILED: "ec服务停止失败,请手动检查",

        StatusCode.STATUS_NOT_DIR_ERROR: "操作对象不是目录",
        StatusCode.STATUS_IS_DIR_ERROR: "操作对象是目录",
        StatusCode.STATUS_FILE_NOT_EXISTS: "文件不存在",
        StatusCode.STATUS_FILE_EXISTS: "文件已存在",
        StatusCode.STATUS_FILE_NOT_IN_SAMEDIR: "文件不在同一个目录",
        StatusCode.STATUS_DIR_NOT_EXISTS: "目录不存在",
        StatusCode.STATUS_DIR_NOT_EMPTY: "目录非空",
        StatusCode.STATUS_SC_IN_USE: "策略正被使用，无法删除",
        StatusCode.STATUS_SC_EXISTS: "存储策略已存在，无法再次创建",
        StatusCode.STATUS_NUMBER_OF_TRASH_FILE_TOO_LARGE: "回收站文件数量过大，请去后台手动执行相关操作",
        StatusCode.STATUS_TRASH_FILE_IS_BEING_DELETED: "正在清空回收站，请稍后再试。",
        StatusCode.STATUS_FILE_NUMBER_IS_TOO_BIG: "文件数量过大，请在后台手动配置。",
        StatusCode.STATUS_SCLASS_NOT_EXISTS: "存储策略不存在",

        StatusCode.STATUS_USER_NOT_EXISTS: "用户不存在",
        StatusCode.STATUS_USER_ALREADY_EXISTS: "用户已存在",
        StatusCode.STATUS_GROUP_NOT_EXISTS: "组不存在",
        StatusCode.STATUS_GROUP_ALREADY_EXISTS: "组已存在",
        StatusCode.STATUS_INVALID_ACTION: "无效的操作",
        StatusCode.STATUS_CHNANGE_PASSWORD_FAILED: "修改密码失败",
        StatusCode.STATUS_INCORRECT_USERNAME_OR_PASSWORD: "无效的用户名或密码",
        StatusCode.STATUS_CREATE_PARTIAL_FAILURE: "部分节点创建失败",
        StatusCode.STATUS_UPDATE_PARTIAL_FAILURE: "部分节点更新失败",
        StatusCode.STATUS_DELETE_PARTIAL_FAILURE: "部分节点删除失败",
        StatusCode.STATUS_UNAUTHORIZED_ACTION: "无权限操作",
        StatusCode.STATUS_ROLE_NOT_EXISTS: "角色不存在",
        StatusCode.STATUS_ROLE_ALREADY_EXISTS: "角色已存在",
        StatusCode.STATUS_ROLE_OCCUPIED: "角色被用户占用",
        StatusCode.STATUS_USER_NOT_SYNCED: "本地用户未同步，请同步",
        StatusCode.STATUS_GROUP_NOT_SYNCED: "本地用户组未同步，请同步",
        StatusCode.STATUS_ANY_ACL_SYNCED_FAILED: "部分节点用户/组同步失败",
        StatusCode.STATUS_ALL_ACL_SYNCED_FAILED: "本地用户/组同步失败",
        StatusCode.STATUS_GID_ALREADY_EXISTS: "用户组GID已存在，请更换",
        StatusCode.STATUS_UID_ALREADY_EXISTS: "用户UID已存在，请更换",
        StatusCode.STATUS_INCORRECT_ORIGINAL_PASSWORD: "原密码错误",

        StatusCode.STATUS_RESOURCES_OCCUPIED: "资源被占用",

        StatusCode.STATUS_SET_FAILED: "设置失败",
        StatusCode.STATUS_EMAIL_CONNECT_FAILED: "邮件服务器连接失败",
        StatusCode.STATUS_EMAIL_AUTH_FAILED: "邮件用户认证失败",
        StatusCode.STATUS_EMAIL_SEND_FAILED: "邮件发送失败",
        StatusCode.STATUS_EMAIL_REFUSED: "邮件被服务端拒收",
        StatusCode.STATUS_EMAIL_NOT_CONFIGURED: "未保存邮件配置",
        StatusCode.STATUS_EMAIL_LEVEL_UNCHECKED: "此告警等级未在邮件中配置",

        StatusCode.STATUS_SNMP_NOT_CONFIGURED:  "未保存SNMP配置",

        # uus
        StatusCode.STATUS_DOMAIN_VIP_OCCUPIED: "保护域VIP已被占用",
        StatusCode.STATUS_DOMAIN_NODE_IP_NOT_EXISTS: "保护域节点IP不存在",
        StatusCode.STATUS_DOMAIN_INIT_ERROR: "保护域初始化失败",
        StatusCode.STATUS_DOMAIN_VIP_CONFIG_ERROR: "保护域VIP配置失败",
        StatusCode.STATUS_DOMAIN_ADD_UUS_FAILED: "保护域添加后续服务失败",
        StatusCode.STATUS_DOMAIN_DELETE_UUS_FAILED: "保护域仍有块服务存在",
        StatusCode.STATUS_DOMAIN_FORCE_REMOVE_LEADER_UUS_ERROR: "保护域强制删除Leader块服务出错",
        StatusCode.STATUS_DOMAIN_FORCE_REMOVE_UUS_ERROR: "保护域强制删除块服务出错",
        StatusCode.STATUS_DOMAIN_FORCE_REMOVE_UUS_FAILED: "保护域强制删除块服务失败",
        StatusCode.STATUS_DOMAIN_SYNC_LIMIT_FAILED: "保护域重构速度应在150~30之间或者等于零",
        StatusCode.STATUS_DOMAIN_HASE_UNREMOVE_UUS: "保护域存在未删除的块服务",
        StatusCode.STATUS_DOMAIN_VIP_REMOVE_FAILED: "保护域VIP删除失败",
        StatusCode.STATUS_DOMAIN_NOT_FOUND: "保护域不存在",
        StatusCode.STATUS_DOMAIN_HASE_OFFLINE_NODE: "保护域中有离线节点",
        StatusCode.STATUS_DOMAIN_ALREADY_EXIST: "保护域已存在",

        StatusCode.STATUS_UUS_UNINITIALIZED: "保护域未初始化存储服务",
        StatusCode.STATUS_UUS_NEED_LICENSE: "块存储服务需要上传license",
        StatusCode.STATUS_UUS_REMOVE_FAILED: "块存储服务删除失败",
        StatusCode.STATUS_UUS_DATABASE_FAILED: "块存储服务数据获取失败",
        StatusCode.STATUS_UUS_DATABASE_STORAGEFAILED: "块存储服务数据存储失败",

        StatusCode.STATUS_POOL_CREATE_FAILED: "存储池创建失败",
        StatusCode.STATUS_POOL_REMOVE_FAILED: "存储池移除失败",
        StatusCode.STATUS_POOL_AUTO_BALANCE_FAILED: "存储池自动均衡失败",
        StatusCode.STATUS_POOL_AUTO_ADD_DISK_FAILED: "存储池自动加盘失败",
        StatusCode.STATUS_POOL_ALLOCATED_FAILED: "存储池预分配虚拟磁盘失败",
        StatusCode.STATUS_POOL_NOT_FOUND: "存储池不存在",
        StatusCode.STATUS_POOL_JOURNAL_CANNOT_REMOVE: "日志池不能删除",
        StatusCode.STATUS_POOL_BALANCE_LIMIT_FAILED: "配置均衡限速失败",
        StatusCode.STATUS_POOL_HASE_NO_DISK: "存储池没有磁盘",
        StatusCode.STATUS_DOMAIN_NOT_HASE_POOL: "保护域没有存储池",

        StatusCode.STATUS_DISK_ADD_TO_POOL_FAILED: "磁盘未能添加到存储池中",
        StatusCode.STATUS_DISK_REMOVE_FROM_POOL_FAILED: "磁盘删除失败",
        StatusCode.STATUS_DISK_ZERO_SUPER_BLOCK_FAILED: "磁盘清除超块失败",
        StatusCode.STATUS_DISK_UPDATE_FAILED: "磁盘更新失败",
        StatusCode.STATUS_DISK_MIGRATE_FAILED: "磁盘迁移失败",
        StatusCode.STATUS_DISK_LIST_IN_POOL_FAILED: "获取存储池磁盘失败",

        StatusCode.STATUS_VDISK_CREATE_FAILED: "虚拟磁盘创建失败",
        StatusCode.STATUS_VDISK_ROLLBACK_FAILED: "虚拟磁盘创建回滚失败",
        StatusCode.STATUS_VDISK_DELETE_FAILED: "虚拟磁盘删除失败, 请检查是否已被使用",
        StatusCode.STATUS_VDISK_NOT_FOUND: "虚拟磁盘不存在",
        StatusCode.STATUS_VDISK_START_FAILED: "虚拟磁盘启动失败",
        StatusCode.STATUS_VDISK_STOP_FAILED: "虚拟磁盘停止失败",
        StatusCode.STATUS_VDISK_THICK_NAMESPACE_FAILED: "厚置备卷失败",
        StatusCode.STATUS_VDISK_ENABLE_JOURNAL_FAILED: "启用日志卷失败",
        StatusCode.STATUS_VDISK_DISABLE_JOURNAL_FAILED: "停用日志卷失败",
        StatusCode.STATUS_VDISK_RAID1_NO_SUPPORT_JOURNAL_FAILED: "raid1不支持日志卷",
        StatusCode.STATUS_VDISK_NAMESPACE_REMOVE_FAILED: "卷删除失败",
        StatusCode.STATUS_VDISK_IS_STOP: "虚拟磁盘未启动",
        StatusCode.STATUS_VDISK_ALREADY_EXISTS: "虚拟磁盘已存在",
        StatusCode.STATUS_VDISK_CAPACITY_UNIT_ERROR: "虚拟磁盘单位错误",
        StatusCode.STATUS_VDISK_CAPACITY_LESS_THAN_ZERO: "虚拟磁盘容量小于等于零",

        StatusCode.STATUS_NAMESPACE_ALREADY_EXISTS: "卷已存在",
        StatusCode.STATUS_NAMESPACE_CREATE_FAILED: "卷创建失败",
        StatusCode.STATUS_NAMESPACE_EXTEND_FAILED: "卷扩容失败",

        StatusCode.STATUS_SNAPSHOT_CREATE_FAILED: "快照创建失败",
        StatusCode.STATUS_SNAPSHOT_DELETE_FAILED: "快照删除失败",
        StatusCode.STATUS_SNAPSHOT_UPDATE_FAILED: "快照更新失败",
        StatusCode.STATUS_SNAPSHOT_DOMAIN_MAX_LIMIT_EXCEEDED: "集群快照上限1024个",
        StatusCode.STATUS_SNAPSHOT_NAMESPACE_MAX_LIMIT_EXCEEDED: "单卷快照上限64个",
        StatusCode.STATUS_SNAPSHOT_ALREADY_EXISTS: "快照已经存在",

        StatusCode.STATUS_ISCSI_CREATE_FAILED: "iSCSI导出创建失败",
        StatusCode.STATUS_ISCSI_ADD_INITIATOR_FAILED: "iSCSI导出添加发起端失败",
        StatusCode.STATUS_ISCSI_DELETE_INITIATOR_FAILED: "iSCSI删除发起端失败",
        StatusCode.STATUS_ISCSI_UPDATE_INITIATOR_FAILED: "iSCSI导出修改发起端失败",
        StatusCode.STATUS_ISCSI_DELETE_FAILED: "iSCSI导出删除失败",
        StatusCode.STATUS_ISCSI_NIC_NOT_FOUND: "iSCSI网卡不存在",
        StatusCode.STATUS_ISCSI_NIC_DELETE_FAILED: "iSCSI网卡删除失败",
        StatusCode.STATUS_ISCSI_UPDATE_CHAP_FAILED: "iSCSI配置chap失败",
        StatusCode.STATUS_ISCSI_DELETE_CHAP_FAILED: "iSCSI删除chap失败",
        StatusCode.STATUS_UUS_SERVER_ATTACH_FAILED: "UUS server 退出维护失败",
        StatusCode.STATUS_UUS_SERVER_DETACH_FAILED: "UUS server 进入维护失败",
        StatusCode.STATUS_UUS_SERVER_ALREADY_ADD: "UUS server 已经添加存在",

        StatusCode.STATUS_ISCSI_INITIATOR_ALREADY_EXISTS: "iSCSI发起端已存在",
        StatusCode.STATUS_ISCSI_LIST_INITIATOR_FAILED: "iSCSI获取发起端失败",
        StatusCode.STATUS_ISCSI_DELETE_VIP_FAILED: "iSCSI删除VIP失败",
        StatusCode.STATUS_ISCSI_SET_VIP_FAILED: "iSCSI配置VIP失败",
        StatusCode.STATUS_ISCSI_GET_VIP_FAILED: "iSCSI获取VIP失败",
        StatusCode.STATUS_ISCSI_SET_NIC_FAILED: "iSCSI配置NIC失败",

        StatusCode.STATUS_NAS_ALREADY_EXISTS: "文件网关服务已存在",
        StatusCode.STATUS_NAS_NOT_EXISTS: "文件网关服务不存在",
        StatusCode.STATUS_NAS_IS_RUNNING: "文件网关服务正在运行",
        StatusCode.STATUS_NAS_UNINITIALIZED: "未初始化文件网关服务",
        StatusCode.STATUS_CES_ALREADY_EXISTS: "高可用服务已存在",
        StatusCode.STATUS_CES_NOT_EXISTS: "高可用服务不存在",
        StatusCode.STATUS_CES_NOT_IN_IP_POOL: "高可用期望IP不在IP池中",
        StatusCode.STATUS_CES_IP_IS_USED: "高可用期望IP已被使用",
        StatusCode.STATUS_CES_POOL_CAN_BE_PINGED: "高可用池内新增IP可PING通",
        StatusCode.STATUS_CES_POOL_LIMIT_REACHED: "高可用IP池的IP个数已达到上限",

        StatusCode.STATUS_NFS_SHARE_ALREADY_EXISTS: "NFS共享已存在",
        StatusCode.STATUS_NFS_SHARE_NOT_EXISTS: "NFS共享不存在",
        StatusCode.STATUS_NFS_SHARE_CLIENT_ALREADY_EXISTS: "共享客户端已存在",
        StatusCode.STATUS_NFS_SHARE_MOUNT_FAILED: "NFS共享挂载失败",
        StatusCode.STATUS_NFS_SHARE_UMOUNT_FAILED: "NFS共享挂载点卸载失败",
        StatusCode.STATUS_NFS_SHARE_SYNCED_FAILED: "部分节点NFS导出同步失败",

        StatusCode.STATUS_CIFS_NAME_ALREADY_EXISTS: "CIFS共享名称已存在",
        StatusCode.STATUS_CIFS_PATH_ALREADY_EXISTS: "CIFS共享路径已存在",
        StatusCode.STATUS_CIFS_SHARE_NOT_EXISTS: "CIFS共享不存在",
        StatusCode.STATUS_CIFS_ACL_USER_NOT_EXISTS: "访问用户不存在",
        StatusCode.STATUS_CIFS_ACL_USER_ALREADY_EXISTS: "访问用户已存在",
        StatusCode.STATUS_CIFS_ACL_GROUP_NOT_EXISTS: "访问组不存在",
        StatusCode.STATUS_CIFS_ACL_GROUP_ALREADY_EXISTS: "访问组已存在",
        StatusCode.STATUS_CIFS_USER_GET_FAILED: "获取CIFS用户数据失败",
        StatusCode.STATUS_CIFS_USER_ADD_FAILED: "添加CIFS用户数据失败",
        StatusCode.STATUS_CIFS_USER_UPDATE_FAILED: "修改CIFS用户数据失败",
        StatusCode.STATUS_CIFS_USER_DETELE_FAILED: "删除CIFS用户数据失败",
        StatusCode.STATUS_CIFS_SHARE_SYNCED_FAILED: "部分节点CIFS共享同步失败",

        StatusCode.STATUS_NAMESERVICE_DOMAIN_CONNECT_FAILED: "AD域连接失败",
        StatusCode.STATUS_NAMESERVICE_AD_TIME_UNSYNC: "主机与AD域时差过大",
        StatusCode.STATUS_NAMESERVICE_CONFIG_WRITE_FAILED: "域相关配置文件写入失败",
        StatusCode.STATUS_NAMESERVICE_AD_HAS_JOINED: "主机已经加入AD域",
        StatusCode.STATUS_NAMESERVICE_AD_JOIN_FAILED: "节点加入AD域失败",
        StatusCode.STATUS_NAMESERVICE_DOMAIN_NOT_CONFIG: "当前集群未加入过域，请先加域",
        StatusCode.STATUS_NAMESERVICE_DOMAIN_NOT_FOUND: "节点已不在域中",
        StatusCode.STATUS_NAMESERVICE_LDAP_CONNECT_FAILED: "LDAP连接失败",
        StatusCode.STATUS_NAMESERVICE_LDAP_JOIN_FAILED: "节点加入LDAP失败",
        StatusCode.STATUS_NAMESERVICE_DOMAIN_SAME_HOSTNAME: "存在相同的hostname",

        StatusCode.STATUS_VOLUME_CACHE_SET: "数据卷设置缓存加速失败",
        StatusCode.STATUS_VOLUME_CACHE_DELETE: "数据卷删除缓存加速失败",
        StatusCode.STATUS_VOLUME_CACHE_GET: "数据卷获取缓存加速失败",

        StatusCode.STATUS_ALERT_CONFIG_ALREADY_EXISTS: "告警配置已存在",
        StatusCode.STATUS_ALERT_CONFIG_NOT_EXISTS: "告警配置不存在",
        StatusCode.STATUS_ALERT_EVENT_NOT_EXISTS: "告警事件不存在",

    }
    return code_tab.get(code, "未知异常: code={}".format(code))
